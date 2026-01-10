from django.contrib.auth.decorators import login_required  # Για προστασία views με login
from django.contrib import messages  # Για μηνύματα επιτυχίας/σφάλματος
from django.shortcuts import render, redirect, get_object_or_404  # Βοηθητικές συναρτήσεις
import pandas as pd  # Για επεξεργασία Excel
from .forms import UploadExcelForm, CustomUserCreationForm, PersonForm, PersonManualForm  # Import forms
from .models import Person, UploadLog  # Import models
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView
from django.db.models.functions import Cast, Func
from django.db.models import IntegerField, Value
from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string


# ============================
# AUTOCOMPLETE VIEWS
# ============================

@login_required
def autocomplete_title(request):
    """AJAX endpoint for title autocomplete"""
    q = request.GET.get('q', '')
    results = (
        Person.objects.filter(titlos__icontains=q)  # Filter titles containing query
        .values_list('titlos', flat=True)
        .distinct()[:10]  # Limit results to 10 unique titles
    )
    return JsonResponse({'results': list(results)})


@login_required
def autocomplete_ekdoths(request):
    """AJAX endpoint for publisher autocomplete"""
    q = request.GET.get('q', '')
    results = (
        Person.objects.filter(ekdoths__icontains=q)
        .values_list('ekdoths', flat=True)
        .distinct()[:10]
    )
    return JsonResponse({'results': list(results)})


# ============================
# HOME & SIGNUP VIEWS
# ============================

def home(request):
    """Render the home page"""
    return render(request, 'home.html')


class SignUpView(CreateView):
    """User registration view"""
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


# ============================
# HELPER FUNCTIONS
# ============================

def clean(value):
    """Clean a cell value from Excel: NaN → None, strip spaces"""
    if pd.isna(value):
        return None
    return str(value).strip()


def clean_ari8mos(value):
    """Clean ΑΡΙΘΜΟΣ ΕΙΣΑΓΩΓΗΣ: convert floats like 115011.0 → '115011'"""
    if pd.isna(value):
        return None
    try:
        return str(int(value))
    except (ValueError, TypeError):
        return str(value).strip()


def generate_koha_from_author(author):
    """Convert 'surname,name' → 'name surname'"""
    if not author or "," not in author:
        return None
    parts = author.split(",")
    if len(parts) != 2:
        return None
    surname = parts[0].strip()
    name = parts[1].strip()
    if not surname or not name:
        return None
    return f"{name} {surname}"


# ============================
# SHOW PEOPLE
# ============================

@login_required
def show_people(request):
    """Display all Person records, ordered by numeric ΑΡΙΘΜΟΣ ΕΙΣΑΓΩΓΗΣ"""
    people = (
        Person.objects
        .exclude(ari8mosEisagoghs__isnull=True)
        .exclude(ari8mosEisagoghs__exact='')
        .annotate(ari8mos_int=Cast('ari8mosEisagoghs', IntegerField()))
        .order_by('ari8mos_int')
    )
    return render(request, 'main/people.html', {'people': people})


# ============================
# UPLOAD EXCEL VIEW
# ============================

@login_required
def upload_excel(request):
    """Handle Excel file upload and processing"""
    if request.method == 'POST':
        form = UploadExcelForm(request.POST, request.FILES)
        if form.is_valid():
            excel_file = request.FILES['excel_file']
            df = pd.read_excel(excel_file)

            existing_ids = set(Person.objects.values_list('ari8mosEisagoghs', flat=True))
            seen_in_file = set()  # Track duplicates within Excel
            added = []
            skipped = []
            duplicates = []
            new_objects = []

            for index, row in df.iterrows():
                ari8mos = clean_ari8mos(row.get('ΑΡΙΘΜΟΣ ΕΙΣΑΓΩΓΗΣ'))
                syggrafeas = clean(row.get('ΣΥΓΓΡΑΦΕΑΣ'))
                koha = clean(row.get('ΣΥΓΓΡΑΦΕΑΣ KOHA')) or generate_koha_from_author(syggrafeas)

                if not ari8mos:
                    skipped.append({'row': index + 2, 'reason': 'Missing ΑΡΙΘΜΟΣ ΕΙΣΑΓΩΓΗΣ'})
                    continue

                # Check for duplicates inside Excel
                if ari8mos in seen_in_file:
                    skipped.append({'row': index + 2, 'reason': 'Duplicate ΑΡΙΘΜΟΣ ΕΙΣΑΓΩΓΗΣ inside Excel'})
                    continue
                seen_in_file.add(ari8mos)

                # Check for duplicates in DB
                if ari8mos in existing_ids:
                    existing_person = Person.objects.filter(ari8mosEisagoghs=ari8mos).first()
                    if not existing_person:
                        # Safe insert if somehow not found
                        new_objects.append(Person(
                            ari8mosEisagoghs=ari8mos,
                            hmeromhnia_eis=clean(row.get('ΗΜΕΡΟΜΗΝΙΑ ΕΙΣΑΓΩΓΗΣ')),
                            syggrafeas=syggrafeas,
                            koha=koha,
                            titlos=clean(row.get('ΤΙΤΛΟΣ')),
                            ekdoths=clean(row.get('ΕΚΔΟΤΗΣ')),
                            ekdosh=clean(row.get('ΕΚΔΟΣΗ')),
                            etosEkdoshs=clean(row.get('ΕΤΟΣ ΕΚΔΟΣΗΣ')),
                            toposEkdoshs=clean(row.get('ΤΟΠΟΣ  ΕΚΔΟΣΗΣ')),
                            sxhma=clean(row.get('ΣΧΗΜΑ')),
                            selides=clean(row.get('ΣΕΛΙΔΕΣ')),
                            tomos=clean(row.get('ΤΟΜΟΣ')),
                            troposPromPar=clean(row.get('ΤΡΟΠΟΣ ΠΡΟΜΗΘΕΙΑΣ ΠΑΡΑΤΗΡΗΣΕΙΣ')),
                            ISBN=clean(row.get('ISBN')),
                            sthlh1=clean(row.get('Στήλη1')),
                            sthlh2=clean(row.get('Στήλη2')),
                        ))
                        existing_ids.add(ari8mos)
                        continue

                    # Real duplicate → store for resolution
                    duplicates.append({
                        "left": {k: getattr(existing_person, k) for k in vars(existing_person) if not k.startswith('_')},
                        "right": {
                            "ari8mos": ari8mos,
                            "hmeromhnia_eis": clean(row.get('ΗΜΕΡΟΜΗΝΙΑ ΕΙΣΑΓΩΓΗΣ')),
                            "syggrafeas": syggrafeas,
                            "koha": koha,
                            "titlos": clean(row.get('ΤΙΤΛΟΣ')),
                            "ekdoths": clean(row.get('ΕΚΔΟΤΗΣ')),
                            "ekdosh": clean(row.get('ΕΚΔΟΣΗ')),
                            "etosEkdoshs": clean(row.get('ΕΤΟΣ ΕΚΔΟΣΗΣ')),
                            "toposEkdoshs": clean(row.get('ΤΟΠΟΣ  ΕΚΔΟΣΗΣ')),
                            "sxhma": clean(row.get('ΣΧΗΜΑ')),
                            "selides": clean(row.get('ΣΕΛΙΔΕΣ')),
                            "tomos": clean(row.get('ΤΟΜΟΣ')),
                            "troposPromPar": clean(row.get('ΤΡΟΠΟΣ ΠΡΟΜΗΘΕΙΑΣ ΠΑΡΑΤΗΡΗΣΕΙΣ')),
                            "ISBN": clean(row.get('ISBN')),
                            "sthlh1": clean(row.get('Στήλη1')),
                            "sthlh2": clean(row.get('Στήλη2')),
                        },
                    })
                    continue

                # Safe insert
                new_objects.append(Person(
                    ari8mosEisagoghs=ari8mos,
                    hmeromhnia_eis=clean(row.get('ΗΜΕΡΟΜΗΝΙΑ ΕΙΣΑΓΩΓΗΣ')),
                    syggrafeas=syggrafeas,
                    koha=koha,
                    titlos=clean(row.get('ΤΙΤΛΟΣ')),
                    ekdoths=clean(row.get('ΕΚΔΟΤΗΣ')),
                    ekdosh=clean(row.get('ΕΚΔΟΣΗ')),
                    etosEkdoshs=clean(row.get('ΕΤΟΣ ΕΚΔΟΣΗΣ')),
                    toposEkdoshs=clean(row.get('ΤΟΠΟΣ  ΕΚΔΟΣΗΣ')),
                    sxhma=clean(row.get('ΣΧΗΜΑ')),
                    selides=clean(row.get('ΣΕΛΙΔΕΣ')),
                    tomos=clean(row.get('ΤΟΜΟΣ')),
                    troposPromPar=clean(row.get('ΤΡΟΠΟΣ ΠΡΟΜΗΘΕΙΑΣ ΠΑΡΑΤΗΡΗΣΕΙΣ')),
                    ISBN=clean(row.get('ISBN')),
                    sthlh1=clean(row.get('Στήλη1')),
                    sthlh2=clean(row.get('Στήλη2')),
                ))
                existing_ids.add(ari8mos)
                added.append({'ari8mos': ari8mos, 'titlos': clean(row.get('ΤΙΤΛΟΣ')), 'syggrafeas': syggrafeas})

            # Bulk create all new Person objects
            Person.objects.bulk_create(new_objects, batch_size=1000)

            # Store duplicates in session for resolve step
            request.session['duplicates'] = duplicates

            # Log upload
            UploadLog.objects.create(
                user=request.user,
                filename=excel_file.name,
                rows_added=len(new_objects),
                rows_updated=0,
            )

            total_records = Person.objects.count()

            return render(request, 'upload_result.html', {
                'added_count': len(new_objects),
                'duplicate_count': len(duplicates),
                'skipped_count': len(skipped),
                'total_records': total_records,
            })
    else:
        form = UploadExcelForm()

    return render(request, 'upload_excel.html', {'form': form})


# ============================
# DUPLICATES RESOLUTION
# ============================

@login_required
def resolve_duplicates(request):
    """Show duplicates from session"""
    duplicates = request.session.get('duplicates', [])
    if not duplicates:
        return render(request, 'main/duplicates_done.html')
    return render(request, 'main/duplicates.html', {'duplicates': duplicates})


@login_required
def handle_duplicate(request):
    """Handle edit/skip action for a single duplicate"""
    if request.method != "POST":
        return redirect("resolve_duplicates")

    ari8mos = request.POST.get("ari8mos")
    action = request.POST.get("action")
    duplicates = request.session.get("duplicates", [])

    # Find the specific duplicate
    dup = next((d for d in duplicates if str(d["left"]["ari8mos"]) == str(ari8mos)), None)
    if not dup:
        return redirect("resolve_duplicates")

    duplicates.remove(dup)
    request.session["duplicates"] = duplicates

    if action == "edit":
        return redirect(f"{reverse('edit_person', args=[ari8mos])}?next=duplicates")
    # action == "skip"
    return redirect("resolve_duplicates")


@login_required
def skip_all_duplicates(request):
    """Skip all duplicates at once"""
    if request.method == "POST":
        request.session['duplicates'] = []
        return redirect('show_people')
    return redirect('resolve_duplicates')


@login_required
def edit_person(request, pk):
    """Edit a single Person record"""
    person = get_object_or_404(Person, pk=pk)
    next_url = request.GET.get('next')

    if request.method == 'POST':
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            messages.success(request, "Record updated successfully.")
            if next_url == 'duplicates':
                return redirect('resolve_duplicates')
            return redirect('show_people')
    else:
        form = PersonForm(instance=person)

    return render(request, 'main/edit_person.html', {'form': form, 'person': person})


# ============================
# ADD PERSON MANUALLY
# ============================

class RegexpReplace(Func):
    """Custom DB function for regex replace in queries"""
    function = 'REGEXP_REPLACE'
    arity = 3


@login_required
def add_person(request):
    """Add a new Person manually, auto-incrementing ΑΡΙΘΜΟΣ ΕΙΣΑΓΩΓΗΣ"""
    last_number = (
        Person.objects
        .exclude(ari8mosEisagoghs__isnull=True)
        .exclude(ari8mosEisagoghs__exact='')
        .annotate(clean_num=Cast(
            RegexpReplace('ari8mosEisagoghs', Value(r'\..*$'), Value('')),
            IntegerField()
        ))
        .order_by('-clean_num')
        .values_list('clean_num', flat=True)
        .first()
    )

    next_number = (last_number or 0) + 1
    submitted = request.GET.get("submitted") == "1"

    if request.method == 'POST':
        form = PersonManualForm(request.POST)
        if form.is_valid():
            person = form.save(commit=False)
            person.ari8mosEisagoghs = str(next_number)
            person.save()
            # POST → REDIRECT → GET
            return redirect(f"{reverse('add_person')}?submitted=1")
    else:
        form = PersonManualForm()

    return render(request, 'main/add_person.html', {'form': form, 'next_number': next_number, 'submitted': submitted})

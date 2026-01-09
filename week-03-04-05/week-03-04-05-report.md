# Week 3 & 4 & 5 💪⌛🗓️

## Introduction

✨ This phase finalizes the Django form workflow by seamlessly combining models, views, templates, authentication, Excel imports, and PostgreSQL. 📚💻
The application is intended solely for internal library staff to manage records securely and efficiently. 🔒📝

---

### Project Structure

This folder appears on the previous page, which is as follows: 🖼️📁

```
php glossa
excel_form_app/
│── manage.py
│── urls.py
│── excel_form_app/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── main/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
│   ├── urls.py
│   └── migrations/
│       └── __init__.py
│
├── templates/
│   ├── base.html
│   ├── home.html
│   └── registration/
|       ├── home.html
│       ├── login.html
│       ├── logged_out.html
│       └── signup.html
│
├── main/templates
|   ├── people.html
│   ├── upload_excel.html
│   ├── upload_result.html
│   ├── upload_success.html
|   └── main/
|       ├── people.html
|       ├── edit_person.html
|       ├── duplicates.html
|       └── duplicates_done.html
```


### 1️⃣ Verify Database Table 🗄️

Open **CMD** as *Admin* and run:

```
python manage.py shell
```
and after

```
from main.models import Person
Person.objects.all()
```

If *no errors* appear, the model and table exist.

Inspect fields:

```
for field in Person._meta.fields:
    print(field.name, field.get_internal_type())
```

👉🏻🗑️ Delete Imported Data (If Needed)

Inside the *same CMD*, run:

```
python manage.py shell
```

and after 

```
from main.models import Person
Person.objects.all().delete()
exit()
```

This step is useful after imports if incorrect data was uploaded.


### 2️⃣ Forms Setup 📝

File: `main/forms.py`

🎯 Purpose:

- 📝 Defines Django forms

- 🔗 Connects directly to the Person model

- ✍️ Used for manual data entry


### 3️⃣ Views Logic 👁️

File: `main/views.py`

👁️ Handles:

- 📄 Listing entries (people.html)

- ✏️ Editing records (edit_person.html)

- 📊 Excel uploads

- 🔍 Duplicate detection

- ✅ Success & result pages


### 4️⃣ URL Configuration 🔗

App-level URLs: `main/urls.py`

Paste the corresponding python code which exists in the week-03 folder 🗂️.

Project-level URLs: `excel_form_app/urls.py`

Ensure the app URLs are included:

```
path('', include('main.urls'))
```


### 5️⃣ Templates are included 🧩

`📂 templates/`
```
registration/
base.html     # Base layout template
home.html     # Landing page template
```

`📂 templates/registration/`
```
home.html        # Authentication home page
login.html       # Login form template
logged_out.html  # Logout confirmation page
signup.html      # User registration page
```

`📂 main/templates/main/`
```
people.html           # Displays all stored records
edit_person.html      # Edit record form
duplicates.html       # Duplicate detection page
duplicates_done.html  # Confirmation page for duplicates handling
```

`📂 main/templates/`
```
main/
people.html          # Alternative or extended listing view
upload_excel.html    # Excel upload form
upload_result.html   # Excel import results page
upload_success.html  # Import success confirmation page
```

### 6️⃣ Manual Entry Test ✅

In the *same CMD*, run:

```
python manage.py runserver
```

Open:

```
http://127.0.0.1:8000/
```

✅ Verify:

- 🌐 people.html loads

- 💾 Entries are saved correctly


### 7️⃣ Install Required Libraries 📦

```
pip install pandas openpyxl
```

Used for Excel (.xlsx) imports.


### 8️⃣ Authentication Setup 🔐

```
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/login/'
```

Create admin user:

```
python manage.py createsuperuser
```


### 9️⃣ Excel Upload Flow 📊

Implemented in: `main/views.py`

✨ Features:

- 📄 Accepts .xlsx only

- 🐼 Uses Pandas

- 🔗 Maps rows to Person model

- 🔍 Detects duplicates


### 🔟 Import Test 🚀

```
python manage.py runserver
```

Login:

```
http://127.0.0.1:8000/login/
```

✅ Verify:

- 🔑 Login works

- 📊 Excel upload succeeds

- 🌐 Records appear in people.html




na bgalo foto to kathe bhma otan tha einai etoimo kai na ta balo edo apo kato

# Week 3 💪⌛🗓️

### Displaying the Database and specifically the Excel in pgadmin and then in the form (on a website)

Create a New Django Project
Run:
django-admin startproject myproject


A new folder named 
myproject
 will be created in your current path. Automatically, a file named 
myproject
 will be created, which contains the files 
settings.py
, 
urls.py
, 
wsgi.py
, 
asgi.py
.
📁 Create a New Django App (in
 
myproject
 folder)

Run:
python manage.py startapp excel_data


A new folder named excel_data will be created inside your project. The folder contains:

models.py
views.py
forms.py
urls.py
templates/

Βήμα 1 — Έλεγξε ότι έχεις Python
Άνοιξε το Command Prompt (cmd) και γράψε:

bash
python --version
ή
Αν σου δείξει έκδοση (π.χ. Python 3.11.7), τότε η Python είναι εγκατεστημένη.


Βήμα 2 — Εγκατάσταση Django
Αν έχεις Python, γράψε:

bash
pip install django

python -m django startproject myproject
Αυτό θα δημιουργήσει φάκελο myproject με το αρχείο manage.py και τον υποφάκελο myproject/.

Έλεγχος
Μόλις τρέξει η εντολή, δες αν δημιουργήθηκε ο φάκελος:

Code
myproject/
    manage.py
    myproject/
        settings.py
        urls.py
        ...

Επόμενο βήμα
Μπες μέσα στον φάκελο:

bash
cd myproject
και φτιάξε το app:

bash
python manage.py startapp books

Βήμα 1 — Δήλωσε το app στο settings.py
Άνοιξε το αρχείο myproject/settings.py και μέσα στο INSTALLED_APPS πρόσθεσε:

python
INSTALLED_APPS = [
    ...,
    'books',
]

myproject/settings.py (DATABASES)
Πήγαινε στο αρχείο myproject/settings.py και βρες το section DATABASES. Αντικατάστησέ το με αυτό:

Βήμα 2 — Φτιάξε το Model
Στο books/models.py βάλε το μοντέλο που ταιριάζει με τις στήλες του Excel σου:

Βήμα 3 — Φτιάξε τη φόρμα για upload
Στο books/forms.py:

Βήμα 4 — Φτιάξε τα Views
Στο books/views.py βάλε:

Βήμα 5 — Templates
Φτιάξε φάκελο books/templates/ και μέσα:

upload_excel.html (φόρμα upload)

list_books.html (πίνακας εμφάνισης)

Σου έδωσα ήδη έτοιμο κώδικα για αυτά.

Βήμα 6 — URLs
Στο books/urls.py:

Στο myproject/urls.py:

Βήμα 8 — Τρέξιμο του server
Στο terminal: 

otan allazeis ton kodika toy models prpei na trexeis kai ayta:
python manage.py makemigrations
python manage.py 

bash
python manage.py runserver

Βήμα 9 — Δοκιμή
Άνοιξε: http://localhost:8000/books/upload/ → θα δεις τη φόρμα για ανέβασμα Excel.

Ανέβασε το Excel σου. kai an den bgalei sfalma tote tha emfanizei Η εισαγωγή ολοκληρώθηκε! kai meta paw sto pgadmin

sto pgadmin. refresh thn vash meta briskeis to table refresh meta view/edit data all rows kai emfanizetai o pinakas me tiw exhs entoles se sql:
SELECT * FROM public.books
ORDER BY id ASC 

me thn entolh 
DELETE FROM books;
diagrafontai ola ta stoixeia otan yparxoyn polles fores se epanalhpsh oi grammes


να βαλω σχολια σε ολους τους κωδικες
παιρναω τον φακελο στο 03-04 και το report apo thn olga
το εχουμε κανει να τρεχει και για κινητα και για υπολογιστες
να γραψω τι αφορα τι
να βγαλω φωτο αυτα που εμφανιζει
ποιους αφορα, τι μπορουν να κανουν για συνδεση και για εγγραφη 
μεταφορτωση αρχειο και τι εμφανιζει + καποιος μπορει να το κανει εκτυπωση 
ο koha εμφανιζεται αυτοματα αφου μπει το ονομα συγγραφεα οταν παει καποιος να προσθεσει καποια επιπλεον εγγραφη 

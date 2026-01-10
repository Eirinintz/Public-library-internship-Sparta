from django import forms
from .models import Person  # Import the Person model
from django.contrib.auth.forms import UserCreationForm  # Import form for creating users
from django.contrib.auth.models import User  # Import Django User model


# Form for creating/editing Person records
class PersonForm(forms.ModelForm):
    class Meta:
        model = Person  # Use the Person model
        fields = [
            'ari8mosEisagoghs',
            'hmeromhnia_eis',
            'syggrafeas',
            'koha',
            'titlos',
            'ekdoths',
            'ekdosh',
            'etosEkdoshs',
            'toposEkdoshs',
            'sxhma',
            'selides',
            'tomos',
            'troposPromPar',
            'ISBN',
            'sthlh1',
            'sthlh2',
        ]  # Fields included in the form


# Custom user registration form
class CustomUserCreationForm(UserCreationForm):
    # Add an email field with validation
    email = forms.EmailField(
        required=True,
        help_text="Required. Enter a valid email address."
    )

    class Meta:
        model = User  # Use Django User model
        fields = ("username", "email", "password1", "password2")  # Fields in the registration form

    # Ensure email is unique
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already registered.")
        return email


# Form for uploading an Excel file
class UploadExcelForm(forms.Form):
    excel_file = forms.FileField(label="")  # File field for Excel


# Manual form for editing Person records, excluding auto-generated entry number
class PersonManualForm(forms.ModelForm):
    class Meta:
        model = Person
        exclude = ['ari8mosEisagoghs']  # Exclude auto-increment field
        widgets = {
            'titlos': forms.Textarea(attrs={'rows': 1}),
            'syggrafeas': forms.Textarea(attrs={'rows': 1}),
            'troposPromPar': forms.Textarea(attrs={'rows': 1}),
            'ekdoths': forms.Textarea(attrs={'rows': 1}),
            'koha': forms.Textarea(attrs={'rows': 1}),
        }  # Textarea widgets with single row for better UI

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

Verify:

- people.html loads
- Entries are saved correctly

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

Features:

- Accepts .xlsx only
- Uses Pandas
- Maps rows to Person model
- Detects duplicates

### 🔟 Import Test 🚀

```
python manage.py runserver
```

Login:

```
http://127.0.0.1:8000/login/
```

Verify:

- Login works
- Excel upload succeeds
- Records appear in `people.html`

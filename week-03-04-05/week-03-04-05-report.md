# Week 3 & 4 & 5 💪⌛🗓️

## Introduction

This phase finalizes the Django form workflow by seamlessly combining models, views, templates, authentication, Excel imports, and PostgreSQL. The application is intended solely for internal library staff to manage records securely and efficiently.

---

### Project Structure

This folder appears on the previous page, which is as follows:

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

1️⃣ Verify Database Table 🗄️

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

2️⃣ Forms Setup 📝

File: `main/forms.py`

Purpose:

- Defines Django forms
- Connects directly to the Person model
- Used for manual data entry

Paste the corresponding python code which is available in the week-03 folder 🗂️.

3️⃣ Views Logic 👁️

File: `main/views.py`

Handles:

- Listing entries (people.html)
- Editing records (edit_person.html)
- Excel uploads
- Duplicate detection
- Success & result pages

There, paste the corresponding python code which is also available in the week-03 folder 🗂️.

4️⃣ URL Configuration 🔗

App-level URLs: `main/urls.py`

Paste the corresponding python code which exists in the week-03 folder 🗂️.

Project-level URLs: `excel_form_app/urls.py`

Ensure the app URLs are included:

```
path('', include('main.urls'))
```

# Week 3 & 4 & 5 💪⌛🗓️

## Introduction

✨ This phase finalizes the Django form workflow by seamlessly combining models, views, templates, authentication, Excel imports, and PostgreSQL. 📚💻
The application is intended solely for internal library staff to manage records securely and efficiently. 🔒📝

---
✅ Once the steps in week-02 are completed, the following actions are performed: 🛠️📂

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

In this specific task:

💻📱 All the code is written in Python and HTML, and the application has been designed to run smoothly on both mobile devices and desktop computers. This ensures a responsive and user-friendly experience across different platforms and screen sizes. 🌐✨


📤 File upload functionality is available, and users can also print the uploaded files when needed. 🖨️


When adding additional records, Koha information appears automatically after entering the author’s name, both during the data entry process and within the database 📚🗄️.
Additionally, entries imported via Excel are added in order, and if someone adds a new record later, it follows the correct sequence in the database, ensuring consistency and reducing manual errors 🔢✨


📚 The application is intended exclusively for library staff and is not designed for public use.
All system messages are displayed in Greek, ensuring clarity, usability, and ease of understanding for internal users. ✨

να βγαλω φωτο αυτα που εμφανιζει
να βαλω σχολια σε ολους τους κωδικες και να δω μηπως αλλαξε καποιον η ολγα
να γραψω το καθενα τι αφορα, τι μπορουν να κανουν για συνδεση και για εγγραφη οι χρηστες

arxikh, h aposyndesh einai to idio me thn arxikh
<img width="1345" height="640" alt="image" src="https://github.com/user-attachments/assets/58579d58-504c-49e4-bb18-04c9c5e150c6" />

eggrafh
<img width="1347" height="630" alt="image" src="https://github.com/user-attachments/assets/325bb6fa-608a-4c5d-a043-699f4fb501c5" />

syndesh 
<img width="1348" height="638" alt="image" src="https://github.com/user-attachments/assets/87f9d663-11f5-4cac-9ddd-58b986d365d5" />

<img width="1346" height="637" alt="image" src="https://github.com/user-attachments/assets/38af136d-be1f-4e63-829a-299042185665" />

eisagogharxeio excel
<img width="1350" height="640" alt="image" src="https://github.com/user-attachments/assets/bb833a4b-2593-48bd-8ed3-a13c56b18bb7" />

prepei na kaneiw micemigrations gia na emfanistei 
<img width="1346" height="639" alt="image" src="https://github.com/user-attachments/assets/bc230244-73db-434e-ba10-86ea44cc9b24" />

<img width="1348" height="635" alt="image" src="https://github.com/user-attachments/assets/ac6a4062-c8dc-486e-9dd5-6e4ab4292660" />

nea eisagogh biblioy
<img width="1365" height="641" alt="image" src="https://github.com/user-attachments/assets/42e4e222-d8ed-4201-aeec-47088ff46bd8" />

oles oi eggrafes
<img width="1347" height="638" alt="image" src="https://github.com/user-attachments/assets/51d8fd44-86fc-4bf0-9564-c1479b0be31c" />

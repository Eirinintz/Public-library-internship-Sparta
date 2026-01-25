# Week 3 & 4 & 5 💪⌛🗓️

## Introduction

✨ This phase finalizes the Django form workflow by seamlessly combining models, views, templates, authentication, Excel imports, and PostgreSQL. 📚💻
The application is intended solely for internal library staff to manage records securely and efficiently. 🔒📝

---

## Project Structure

The folder `Project 1` appears on the previous page, which is as follows: 🖼️📁

```
Project 1/
└── static/main
│        └── autocomplete.js
│── manage.py
│── requirements.txt
│── urls.py

│
│── excel_form_app/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
|   └── static/main
│        └── autocomplete.js
|
├── main/
    └── migrations/
│       └── __init__.py
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
│   ├── urls.py
│   
|
├── main/templates
    ├── incomplete_records.html
│   ├── upload_excel.html
│   ├── upload_result.html
│   ├── upload_success.html
|   └── main/
|       ├── add_person.html
        ├── autocomplete.js
|       ├── people.html
        ├── people_table_rows.html
        ├── print_range.html
        ├── resolve_duplicates.html
|       ├── edit_person.html
|       └── duplicates_done.html
|
├── main/static
|   ├── images/
|       └── books_background.jpg
│
├── templates/
│   ├── base.html
│   ├── home.html
│   └── registration/
|       ├── home.html
│       ├── login.html
│       ├── logged_out.html
│       └── signup.html
```

---

## 🌐 To run the web application locally, follow these steps: 🛠️💻

### 1️⃣ Open the command prompt and navigate to your project folder

Run **CMD** as *Admin*:
```
cd <your_project_folder>
```

### 2️⃣ Create a *virtual environment* and activate it

In the *same CMD*, run:
```
python -m venv venv
```
and 
```
venv\Scripts\activate
```

### 3️⃣ Install required libraries

And after:

```
pip install django
```
```
pip install psycopg2-binary
```
```
pip install pandas openpyxl
```

### 4️⃣ Apply database migrations

Then:

```
python manage.py makemigrations
```
and
```
python manage.py migrate
```

💡 Tip: Make sure your PostgreSQL database is running and your settings in settings.py are correct before running migrations. 🐘✅

### 5️⃣ Start the development server

And after this:

```
python manage.py runserver
```

### 6️⃣ Finish

Open your browser and go to:

```
http://127.0.0.1:8000/ 
```

---

In this specific task:

💻📱 All the code is written in Python and HTML, and the application has been designed to run smoothly on both mobile devices and desktop computers. This ensures a responsive and user-friendly experience across different platforms and screen sizes. 🌐✨


📤 File upload functionality is available, and users can also print the uploaded files when needed. 🖨️


When adding additional records, Koha information appears automatically after entering the author’s name, both during the data entry process and within the database 📚🗄️.
Additionally, entries imported via Excel are added in order, and if someone adds a new record later, it follows the correct sequence in the database, ensuring consistency and reducing manual errors 🔢✨


📚 The application is intended exclusively for library staff and is not designed for public use.
All system messages are displayed in Greek, ensuring clarity, usability, and ease of understanding for internal users. ✨

---

## 🌐 Below, I present the website we created: 🖥️✨


### 🏠 Home / Logout

The logout page is the same as the home page, providing a consistent interface for users. 🔄✨


<img width="1345" height="640" alt="image" src="https://github.com/user-attachments/assets/58579d58-504c-49e4-bb18-04c9c5e150c6" />


### 📝 Registration / Signup

Users can create a new account by filling out the registration form. 🔐✨

All fields are validated to ensure correct input before submission. ✅


<img width="1347" height="630" alt="image" src="https://github.com/user-attachments/assets/325bb6fa-608a-4c5d-a043-699f4fb501c5" />


### 🔑 Login / Sign In

Users can log in to their account by entering their username and password. 🖥️💻


<img width="1348" height="638" alt="image" src="https://github.com/user-attachments/assets/87f9d663-11f5-4cac-9ddd-58b986d365d5" />


Successful login redirects the user to the home page, while incorrect credentials display an error message ❌⚠️.


<img width="1346" height="637" alt="image" src="https://github.com/user-attachments/assets/38af136d-be1f-4e63-829a-299042185665" />



### 📊 Excel Upload / Data Import

Users can upload an Excel file (.xlsx) to import multiple records at once into the database. 🗂️💾

- The system reads the Excel file using Pandas 🐼

- Each row is mapped to the Person model 🔗

- Duplicate entries are automatically detected 🔍

- After successful import, a confirmation message is displayed ✅

  
<img width="1350" height="640" alt="image" src="https://github.com/user-attachments/assets/bb833a4b-2593-48bd-8ed3-a13c56b18bb7" />


⚠️ You need to run makemigrations and migrate for the database tables to appear 🗄️✨


<img width="1346" height="639" alt="image" src="https://github.com/user-attachments/assets/bc230244-73db-434e-ba10-86ea44cc9b24" />


<img width="1348" height="635" alt="image" src="https://github.com/user-attachments/assets/ac6a4062-c8dc-486e-9dd5-6e4ab4292660" />


### 📚 Add New Book / New Entry

Users can add a new book record to the database by filling out the form with details such as:

- Author ✍️

- Title 📖

- Publication Year 🗓️

- Other relevant fields 📝

- Koha information appears automatically after entering the author’s name 🔍

- Entries imported via Excel follow the correct sequence, and any new record added manually will be inserted in order 🔢

- Ensures consistency and reduces manual errors ✅


<img width="1365" height="641" alt="image" src="https://github.com/user-attachments/assets/42e4e222-d8ed-4201-aeec-47088ff46bd8" />


### 🗃️ All Records / Database Entries

The application allows library staff to manage all book/person records efficiently.


<img width="1346" height="636" alt="image" src="https://github.com/user-attachments/assets/99a4d880-c96f-4723-8790-4123d2f34654" />

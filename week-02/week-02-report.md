# Week 2💪⌛🗓️

## 🌐 Combining a Web Server with PHP and MySQL

Last week I worked with MySQL, Web Server, Python and Php.

This week, we will integrate PHP with MySQL and Web Server.

---

### 🐘 Setting up phpMyAdmin 

### 1️⃣ ⬇️ Download phpMyAdmin (all languages) last version

Link: https://www.phpmyadmin.net/downloads/

Extract all files to: 
```
C:/Apache24/htdocs/phpmyadmin
```

### 2️⃣ 📄 Copy config file

Copy **config.sample.inc.php** → **config.inc.php**

Do not add an extra .php extension.

### 3️⃣ 🔑 Set blowfish_secret

Open **config.inc.php** and go to line 16 and add a random 32-character key and save the file.

### 4️⃣ ⚙️ Edit httpd.conf for PHP

Replace/add lines at the end of **httpd.conf** in your computer, which is in the **httpd.conf** code:

### 5️⃣ 🛠 Edit php.ini

Copy **php.ini-production** → **php.ini** in `C:/php`

production -> Server, development -> locally

Enable required extensions by removing the ; from the following:

*extension=mysqli*

*extension=pdo_mysql*

### 6️⃣ 🚀 Start Apache with the following:

```
cd C:/Apache24/bin
```
```
httpd -k start
```

### 7️⃣ 🌐 Open phpMyAdmin

Go to: 

```
http://localhost/phpmyadmin
```

You should see the login form. Username & password → MySQL credentials.

---

### 🗂 Creating a Database in phpmyadmin

### 1️⃣ 🆕 Create a new database

In the left column of phpMyAdmin → click Create database → give it a name.

### 2️⃣ 📊 Import data from Excel

Convert Excel to CSV.

Upload it to phpMyAdmin → set delimiter (; instead of ,) → click Import.

💡 Tip: Make sure column names in CSV match your database fields.

---

### 🐍 Installing Django

### 1️⃣ 🔍 Check Python version

Open **CMD (Run as Administrator)** and run:

```
python --version
```

- If Python is not installed, download and install it from the official website.

- If the command prints a version number, you're good to go ✔️.

### 2️⃣ ⚡ Create virtual environment

In the same CMD, navigate to your desired directory and run:

```
python -m venv venv
```

### 3️⃣ 🚀 Activate virtual environment (Always)

Activate it:

```
venv\Scripts\activate
```
and then it will appear in front of *venv*

### 4️⃣ 📦 Install Django

Navigate to your working directory:

```
cd C:\Users\...
```

Then install Django:

```
pip install django
```

✅ If installation completes successfully, continue to the next step.

### 5️⃣ 📁 Create Django project

Run:

```
django-admin startproject Project 1
```

A new folder named Project 1 will be created in your current path. Automatically, a file named excel_form_app will be created, which contains the files:

- settings.py
- urls.py
- wsgi.py
- asgi.py

Move into the project directory:

```
cd Project 1
```

### 6️⃣ 🏃 Run Django development server

Start the Django server:

```
python manage.py runserver
```

Open the URL it provides (e.g., http://127.0.0.1:8000)

You will see a rocket 🚀 icon indicating the server is running.

Stop the server anytime with:

```
Ctrl + C
```

The files manage.py and db.sqlite3 must be located in the root directory created by the user. 

Keeping them in the initial folder ensures that Django can properly manage the project and database.


### 7️⃣ 💻 Open project in Visual Studio Code

Run:

```
code .
```
This will open Project 1 in Visual Studio Code for development.

---

### 🚀 PostgreSQL Installation (pgadmin) & Database Setup Guide

### 1️⃣ 🛠️ Install PostgreSQL
- Download the PostgreSQL for *Windows* installer from the official website: https://www.enterprisedb.com/downloads/postgres-postgresql-downloads. 📥
- Run the installer and click **Next** on all steps. 👉
- Leave all default components selected. ✔️
  - PostgreSQL Server
  - pgAdmin 4
  - Stack Builder
- Choose an installation folder (or leave the default path). 📁
- Enter a **password for the `postgres` superuser**. 🔐
- Keep the default **Port: 5432**. 🌐
- Leave Locale as **Default**. 🌍
- Click **Next → Next → Install → Finish**. 🎉

### 2️⃣❌ Stack Builder
When the Stack Builder window appears:

Click **Cancel** (it is not required for the basic installation). 🙅‍♂️

### 3️⃣🔎 Verify PostgreSQL Service

You can optionally check that the PostgreSQL service is running:

- Open **Services** (Windows Start → type *Services*). 🖥️
- Locate **postgresql-x64-18** (or similar version). 📌
- Ensure the **Status** is **Running**. 🟢
- If not, right-click → **Start**. ▶️

### 4️⃣ 🧰 Open pgAdmin
- Launch **pgAdmin** from the Start Menu. 🚀
- Set a **master password** (used only by pgAdmin). 🔑
- Click on the PostgreSQL server. 🗄️
- Enter the **password you set during PostgreSQL installation**. ✔️

### 5️⃣ 🗃️ Create a New Database
- In the left sidebar, expand **Servers → PostgreSQL → Databases**. 📂
- Right-click **Databases** → **Create → Database…** ➕
- Enter a **Database Name** (e.g., `mydatabase`). ✏️
- Click **Save**. 💾

### 🎉 Your PostgreSQL server and database are now ready to use! 🚀

---

### Connecting Django + PostgreSQL Setup Guide

### 🚀 Activate virtual environment (Always)

In the Beginning:

```
venv\Scripts\activate`
```

and after

```
cd Project 1
```

### 🖥 Start the Django Server

In **CMD** run:

```
python manage.py runserver
```

The server should run **without any errors** 🚀.

### 1️⃣ Install PostgreSQL Driver

In the same terminal where your `manage.py` file is located, run:

```
pip install psycopg2-binary
```

✔ If it installs successfully, continue to the next step.

### 2️⃣ PostgreSQL Database Credentials

Make sure you have a database created in pgAdmin with these settings:

* **Database name:** `db`
* **User:** `postgres`
* **Password:** (the one you set when installing PostgreSQL) 🔐
* **Host:** `localhost`
* **Port:** `5432`

These values will be used by Django.

### 3️⃣ Configure Django to Use PostgreSQL

Open your Django project’s `settings.py` file and find the `DATABASES = { ... }` block.

Replace it with:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'db',
        'USER': 'postgres',
        'PASSWORD': 'your_database_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```
and save the file.

⚠️ Note: The database name given by the user in pgAdmin 4 needs to be the same as the one set in the settings.py code.

🎯 This connects Django to your PostgreSQL server.

### 4️⃣ Run Initial Migrations

Create Django’s core tables inside PostgreSQL, in the same terminal::

```
python manage.py migrate
```

✔ If no errors appear, the database connection works! 🎉

### 5️⃣ Create the Django App for Excel Handling

Inside the Project 1, run:

```
python manage.py startapp main 
```

A new folder named main will be created inside your project. The folder contains:

- models.py
- views.py
- forms.py
- urls.py
- templates/

### 6️⃣ Register the App in Django Settings

Open `settings.py` again and add your new app to `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main'
]
```
and save the file.

⚠️ Do NOT add the database name (`mydb`).
Only Django apps go here — not databases.

### 7️⃣ Add Your Models

Open:

```
main/models.py
```

Replace its content with the code **models.py** and save the file 💾.

⚠️ This specific code refers to the library manuals, covering the needs of the Sparta public library.

### 8️⃣ Create and Apply Model Migrations

Run the following:

```
python manage.py makemigrations
```

and after

```
python manage.py migrate
```

✔ New tables will be created in your PostgreSQL database 🗃️.

⚠️makemigrations and migrate must be executed whenever changes are made to the database schema (models), such as adding, removing, or modifying model fields or models.

### 9️⃣ Verify Everything

### 🔍 In pgAdmin:

You should now see:

*Servers → Databases → db → Schemas → public → Tables*

Your tables should be visible there 👀.

### 🎉 Finished!

Your Django project is now fully connected to PostgreSQL, your app is registered, migrations are applied, and the database is ready to receive Excel data.

✅ You can now start implementing Excel import functionality using this setup.





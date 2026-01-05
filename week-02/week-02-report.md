# Week 2💪⌛🗓️

## 🌐 Combining a Web Server with PHP and MySQL

Last week I worked with MySQL, Web Server, Python and Php.

This week, we will integrate PHP with MySQL and Web Server.

---

### 🐘 Setting up phpMyAdmin 

#### 1️⃣ ⬇️ Download phpMyAdmin (all languages) last version

Link: https://www.phpmyadmin.net/downloads/

Extract all files to: 
```
C:/Apache24/htdocs/phpmyadmin
```

#### 2️⃣ 📄 Copy config file

Copy **config.sample.inc.php** → **config.inc.php**

Do not add an extra .php extension.

#### 3️⃣ 🔑 Set blowfish_secret

Open **config.inc.php** and go to line 16 and add a random 32-character key and save the file.

#### 4️⃣ ⚙️ Edit httpd.conf for PHP

Replace/add lines at the end of **httpd.conf** in your computer, which is in the **httpd.conf** code:

#### 5️⃣ 🛠 Edit php.ini

Copy **php.ini-production** → **php.ini** in `C:/php`

production -> Server, development -> locally

Enable required extensions by removing the ; from the following:

*extension=mysqli*

*extension=pdo_mysql*

#### 6️⃣ 🚀 Start Apache with the following:

```
cd C:/Apache24/bin
```
```
httpd -k start
```

#### 7️⃣ 🌐 Open phpMyAdmin

Go to: 

```
http://localhost/phpmyadmin
```

You should see the login form. Username & password → MySQL credentials.

---

### 🗂 Creating a Database in phpmyadmin

#### 1️⃣ 🆕 Create a new database

In the left column of phpMyAdmin → click Create database → give it a name.

#### 2️⃣ 📊 Import data from Excel

Convert Excel to CSV.

Upload it to phpMyAdmin → set delimiter (; instead of ,) → click Import.

💡 Tip: Make sure column names in CSV match your database fields.

---

### 🐍 Installing Django

#### 1️⃣ 🔍 Check Python version

Open **CMD** and run:

```
python --version
```

#### 2️⃣ ⚡ Create virtual environment

```
python -m venv venv
```

#### 3️⃣ 🚀 Activate virtual environment (Always)

```
venv\Scripts\activate
```

#### 4️⃣ 📦 Install Django

```
pip install django
```

#### 5️⃣ 📁 Create Django project

```
django-admin startproject myproject
```

#### 6️⃣ 🏃 Run Django development server

```
cd myproject
```

```
python manage.py runserver
```

Open the URL it provides (e.g., http://127.0.0.1:8000)

You will see a rocket 🚀 icon indicating the server is running.

#### 7️⃣ 🛠 Create Django app 

For example, run:

```
python manage.py startapp my_app
```

This will create a folder my_app inside myproject.

#### 8️⃣ 💻 Open project in Visual Studio Code

```
code .
```

This open the file *myproject* in Visual Studio Code.

---

### 🚀 PostgreSQL Installation (pgadmin) & Database Setup Guide

#### 1️⃣ 🛠️ Install PostgreSQL
- Download the PostgreSQL installer from the official website: https://www.enterprisedb.com/downloads/postgres-postgresql-downloads. 📥
- Run the installer and click **Next** on all steps. 👉
- Leave all default components selected. ✔️
- Choose an installation folder (or leave the default path). 📁
- Enter a **password for the `postgres` superuser**. 🔐
- Keep the default **Port: 5432**. 🌐
- Leave Locale as **Default**. 🌍
- Click **Next → Next → Install → Finish**. 🎉

#### 2️⃣❌ Stack Builder
When the Stack Builder window appears:

Click **Cancel** (it is not required for the basic installation). 🙅‍♂️

#### 3️⃣🔎 Verify PostgreSQL Service
- Open **Services** (Windows Start → type *Services*). 🖥️
- Locate **postgresql-x64-18** (or similar version). 📌
- Ensure the **Status** is **Running**. 🟢
- If not, right-click → **Start**. ▶️

#### 4️⃣ 🧰 Open pgAdmin
- Launch **pgAdmin** from the Start Menu. 🚀
- Set a **master password** (used only by pgAdmin). 🔑
- Click on the PostgreSQL server. 🗄️
- Enter the **password you set during PostgreSQL installation**. ✔️

#### 5️⃣ 🗃️ Create a New Database
- In the left sidebar, expand **Servers → PostgreSQL → Databases**. 📂
- Right-click **Databases** → **Create → Database…** ➕
- Enter a **Database Name** (e.g., `mydatabase`). ✏️
- Click **Save**. 💾

#### 🎉 Your PostgreSQL server and database are now ready to use! 🚀

---

### 🚀 Django + PostgreSQL Setup Guide

#### 🚀 Activate virtual environment (Always)

In the Beginning:

```
venv\Scripts\activate`
```
and after

```
cd myproject
```

#### 🖥 Start the Django Server

```
python manage.py runserver
```

The server should run **without any errors** 🚀.

#### 1️⃣ Install PostgreSQL Driver

In the same terminal where your `manage.py` file is located, run:

```
pip install psycopg2-binary
```

✔ If it installs successfully, continue.

#### 2️⃣ PostgreSQL Database Credentials

Make sure you have a database created in pgAdmin with these settings:

* **Database name:** `db`
* **User:** `postgres`
* **Password:** (the one you set when installing PostgreSQL) 🔐
* **Host:** `localhost`
* **Port:** `5432`

These values will be used by Django.

#### 3️⃣ Configure Django to Use PostgreSQL

Open your Django project’s `settings.py` file and find the `DATABASES = { ... }` block.
Replace it with:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'db',
        'USER': 'postgres',
        'PASSWORD': 'your_postgres_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```
and save.

The Database Name should be the same everywhere

🎯 This connects Django to your PostgreSQL server.

#### 4️⃣ Run Initial Migrations

Create Django’s core tables inside PostgreSQL:

```
python manage.py migrate
```

✔ If no errors appear, the database connection works! 🎉

#### 5️⃣ Create the Django App for Excel Handling

Run:

```
python manage.py startapp excel_data
```

A new folder named `excel_data` will appear 📁.

#### 6️⃣ Register the App in Django Settings

Open `settings.py` again and add your new app to `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    ...,
    'excel_data',
]
```
and save.
⚠️ Do NOT add the database name (`mydb`).
Only Django apps go here — not databases.

#### 7️⃣ Add Your Models

Open:

```
excel_data/models.py
```

Replace its content with the code **models.py**.
Save the file 💾.

These models define the structure of the tables that will store your Excel data.

⚠️ This specific code refers to the library manuals, covering the needs of the Sparta public library.

#### 8️⃣ Create and Apply Model Migrations

Run the following:

```
python manage.py makemigrations
```
```
python manage.py migrate
```

✔ New tables will be created in your PostgreSQL database 🗃️.

#### 9️⃣ Verify Everything

#### 🔍 In pgAdmin:

You should now see:

*Servers → Databases → db → Schemas → public → Tables*

Your tables should be visible there 👀.

### 🎉 Finished!

Your Django project is now fully connected to PostgreSQL, your app is registered, migrations are applied, and the database is ready to receive Excel data.

✅ You can now start implementing Excel import functionality using this setup.















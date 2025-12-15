# Week 2💪⌛🗓️

## 🌐 Combining a Web Server with PHP and MySQL

Last week I worked with MySQL and a Web Server.

This week, we will integrate PHP with the two above.

---

### 🐘 Setting up phpMyAdmin 

#### 1️⃣ ⬇️ Download phpMyAdmin (all languages) last version

Extract all files to: `C:/Apache24/htdocs/phpmyadmin`

#### 2️⃣ 📄 Copy config file

Copy **config.sample.inc.php** → **config.inc.php**

Do not add an extra .php extension.

#### 3️⃣ 🔑 Set blowfish_secret

Open **config.inc.php** and go to line 16 and add a random 32-character key and save the file.

#### 4️⃣ ⚙️ Edit httpd.conf for PHP

Replace/add these lines at the end of **httpd.conf** in your computer:

`LoadModule php_module c:/php/php8apache2_4.dll`

`AddType application/x-httpd-php .php`

`PHPIniDir C:/php`

#### 5️⃣ 🛠 Edit php.ini

Copy **php.ini-production** → **php.ini** in `C:/php`

production -> Server, development -> locally

Enable required extensions by removing the ; from the following:

*extension=mysqli*

*extension=pdo_mysql*

#### 6️⃣ 🚀 Start Apache with the following:

`cd C:/Apache24/bin`

`httpd -k start`

#### 7️⃣ 🌐 Open phpMyAdmin

Go to: `http://localhost/phpmyadmin`

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

`python --version`

#### 2️⃣ ⚡ Create virtual environment

`python -m venv venv`

#### 3️⃣ 🚀 Activate virtual environment (Always)

`venv\Scripts\activate`

#### 4️⃣ 📦 Install Django

`pip install django`

#### 5️⃣ 📁 Create Django project

`django-admin startproject myproject`

#### 6️⃣ 🏃 Run Django development server

`cd myproject`

`python manage.py runserver`

Open the URL it provides (e.g., http://127.0.0.1:8000)

You will see a rocket 🚀 icon indicating the server is running.

#### 7️⃣ 🛠 Create Django app

`python manage.py startapp my_app`

This will create a folder my_app inside myproject.

#### 8️⃣ 💻 Open project in Visual Studio Code

`code .`

Open both *myproject* and *my_app* in Visual Studio Code.

---

### 🚀 PostgreSQL Installation (pgadmin) & Database Setup Guide

#### 1. 🛠️ Install PostgreSQL
1. Download the PostgreSQL installer from the official website. 📥
2. Run the installer and click **Next** on all steps. 👉
3. Leave all default components selected. ✔️
4. Choose an installation folder (or leave the default path). 📁
5. Enter a **password for the `postgres` superuser**. 🔐
6. Keep the default **Port: 5432**. 🌐
7. Leave Locale as **Default**. 🌍
8. Click **Next → Next → Install → Finish**. 🎉

#### 2. ❌ Stack Builder
When the Stack Builder window appears:

Click **Cancel** (it is not required for the basic installation). 🙅‍♂️

#### 3. 🔎 Verify PostgreSQL Service
1. Open **Services** (Windows Start → type *Services*). 🖥️
2. Locate **postgresql-x64-18** (or similar version). 📌
3. Ensure the **Status** is **Running**. 🟢
4. If not, right-click → **Start**. ▶️

#### 4. 🧰 Open pgAdmin
1. Launch **pgAdmin** from the Start Menu. 🚀
2. Set a **master password** (used only by pgAdmin). 🔑
3. Click on the PostgreSQL server. 🗄️
4. Enter the **password you set during PostgreSQL installation**. ✔️

#### 5. 🗃️ Create a New Database
1. In the left sidebar, expand **Servers → PostgreSQL → Databases**. 📂
2. Right-click **Databases** → **Create → Database…** ➕
3. Enter a **Database Name** (e.g., `mydatabase`). ✏️
4. Click **Save**. 💾

#### 🎉 Your PostgreSQL server and database are now ready to use! 🚀

---

### 🚀 Django + PostgreSQL Setup Guide

#### (Preparation for Excel Import Into Database)

#### 1️⃣ Install PostgreSQL Driver

In the same terminal where your `manage.py` file is located, run:

```bash
pip install psycopg2-binary
```

✔ If it installs successfully, continue.

#### 2️⃣ PostgreSQL Database Credentials

Make sure you have a database created in pgAdmin with these settings:

* **Database name:** `mydb`
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
        'NAME': 'mydb',
        'USER': 'postgres',
        'PASSWORD': 'your_postgres_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

🎯 This connects Django to your PostgreSQL server.

#### 4️⃣ Run Initial Migrations

Create Django’s core tables inside PostgreSQL:

```bash
python manage.py migrate
```

✔ If no errors appear, the database connection works! 🎉

#### 5️⃣ Create the Django App for Excel Handling

Run:

```bash
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

⚠️ Do NOT add the database name (`mydb`).
Only Django apps go here — not databases.

#### 7️⃣ Add Your Models

Open:

```
excel_data/models.py
```

Replace its content with your model definitions.
Save the file 💾.

These models define the structure of the tables that will store your Excel data.

#### 8️⃣ Create and Apply Model Migrations

Run the following:

```bash
python manage.py makemigrations
python manage.py migrate
```

✔ New tables will be created in your PostgreSQL database 🗃️.

#### 9️⃣ Verify Everything

#### 🔍 In pgAdmin:

You should now see:

```
Servers → Databases → mydb → Schemas → public → Tables
```

Your tables should be visible there 👀.

#### 🖥 Start the Django Server

```bash
python manage.py runserver
```

The server should run **without any errors** 🚀.

### 🎉 Finished!

Your Django project is now fully connected to PostgreSQL, your app is registered, migrations are applied, and the database is ready to receive Excel data.

✅ You can now start implementing Excel import functionality using this setup.















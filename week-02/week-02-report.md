# Week 2💪⌛🗓️

## 🌐 Combining a Web Server with PHP and MySQL

Last week I worked with MySQL and a Web Server.

This week, we will integrate PHP with the two above.

---

### 🐘 Setting up phpMyAdmin (PHP + MySQL)

#### 1️⃣ ⬇️ Download phpMyAdmin (all languages)

Extract all files to: `C:/Apache24/htdocs/phpmyadmin`

#### 2️⃣ 📄 Copy config file

Copy **config.sample.inc.php** → **config.inc.php**

Do not add an extra .php extension.

#### 3️⃣ 🔑 Set blowfish_secret

Open **config.inc.php** and go to line 16 and add a random 32-character key and save the file.

#### 4️⃣ ⚙️ Edit httpd.conf for PHP

Replace/add these lines at the end of **httpd.conf**:

`LoadModule php_module c:/php/php8apache2_4.dll`

`AddType application/x-httpd-php .php`

`PHPIniDir C:/php`

#### 5️⃣ 🛠 Edit php.ini

Copy **php.ini-production** → **php.ini** in `C:/php`

Enable required extensions by removing the ; from the following:

*extension=mysqli*

*extension=pdo_mysql*

#### 6️⃣ 🚀 Start Apache

`cd C:/Apache24/bin`

`httpd -k start`

#### 7️⃣ 🌐 Open phpMyAdmin

Go to: `http://localhost/phpmyadmin`

You should see the login form. Username & password → MySQL credentials.

---

### 🗂 Creating a Database

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


#### 3️⃣ 🚀 Activate virtual environment

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

#### 8️⃣ 💻 Open project in VS Code

`code .`

Open both myproject and my_app in VS Code.

---

### 🚀 PostgreSQL Installation & Database Setup Guide

#### 1. 🛠️ Install PostgreSQL
1. Download the PostgreSQL installer from the official website. 📥
2. Run the installer and click **Next** on all steps. 👉
3. Leave all default components selected. ✔️
4. Choose an installation folder (or leave the default path). 📁
5. Enter a **password for the `postgres` superuser**. 🔐
6. Keep the default **Port: 5432**. 🌐
7. Leave Locale as **Default**. 🌍
8. Click **Next → Next → Install → Finish**. 🎉

---

#### 2. ❌ Stack Builder
When the Stack Builder window appears:
- Click **Cancel** (it is not required for the basic installation). 🙅‍♂️

---

#### 3. 🔎 Verify PostgreSQL Service
1. Open **Services** (Windows Start → type *Services*). 🖥️
2. Locate **postgresql-x64-18** (or similar version). 📌
3. Ensure the **Status** is **Running**. 🟢
4. If not, right-click → **Start**. ▶️

---

#### 4. 🧰 Open pgAdmin
1. Launch **pgAdmin** from the Start Menu. 🚀
2. Set a **master password** (used only by pgAdmin). 🔑
3. Click on the PostgreSQL server. 🗄️
4. Enter the **password you set during PostgreSQL installation**. ✔️

---

#### 5. 🗃️ Create a New Database
1. In the left sidebar, expand **Servers → PostgreSQL → Databases**. 📂
2. Right-click **Databases** → **Create → Database…** ➕
3. Enter a **Database Name** (e.g., `mydatabase`). ✏️
4. Click **Save**. 💾

#### 🎉 Your PostgreSQL server and database are now ready to use! 🚀

---

### σύνδεση django με PostgreSQL (gia import excel kai oxi me python)

στο ίδιο cmd (εκεί που υπάρχει δλδ το manage.py) γράψε: 

pipe install psycopg2 -binary , αν είναι οκ συνεχίζουμε 

τα στοιχεία της βάσης:

Database name: mydb

user: postgres

Pass word: τον κωδικό που έβαλες κατά την εγκατάσταση του PostgreSQL 

host: Localhost 

Port: 5432

άνοιξε το αρχείο settings.py

στο σημείο Database={.....}

αντικατέστησε από το σημείο 'Name': 'mydb', 

όταν τελειώσεις με τα παραπάνω, στο ίδιο cmd τρέξε: 

python manage.py migrate για να δημιουργήσει tables στη βάση 

Στο cmd: python manage.py startapp excel_data με την οποία δημιουργείται ο φάκελος "excel_data"

στα settings βρες το INSTALLED_APPS και πρόσθεσε τη γραμμή 'mydb', στο τέλος και αποθήκευσε

Στον φάκελο αυτόν, υπάρχει το models.py και άνοιξε το στο visual και αντικατέστησε το με τον κώδικα .... και save 

Στο cmd python manage.py makemigrations

python manage.py migrate 

Όποτε θα εμφανίζονται τα εξής:

Είναι παντού οκ 

Servers Databases mydata shima public tables βλέπεις όλους τους πίνακες 

τρέχει ο django server χωρίς να κάνει λάθη 

### Ανάδειξη excel στο localhost χρησιμοποιωστας python













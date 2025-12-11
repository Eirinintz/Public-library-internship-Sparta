## 🌐 Combining a Web Server with PHP and MySQL

Last week I worked with MySQL and a Web Server.
This week, we will integrate PHP with the two above.

---

🐘 Setting up phpMyAdmin (PHP + MySQL)

⬇️ Download phpMyAdmin (all languages)

Extract all files to: `C:/Apache24/htdocs/phpmyadmin`

📄 Copy config file

Copy config.sample.inc.php → config.inc.php

Do not add an extra .php extension.

🔑 Set blowfish_secret

Open config.inc.php

Go to line 16 and add a random 32-character key

Save the file.

⚙️ Edit httpd.conf for PHP

Replace/add these lines at the end of httpd.conf:

LoadModule php_module c:/php/php8apache2_4.dll
AddType application/x-httpd-php .php
PHPIniDir C:/php


🛠 Edit php.ini

Copy php.ini-production → php.ini in C:/php

Enable required extensions by removing the ;:

extension=mysqli
extension=pdo_mysql


🚀 Start Apache

cd C:/Apache24/bin
httpd -k start


🌐 Open phpMyAdmin

Go to: http://localhost/phpmyadmin

You should see the login form.

Username & password → MySQL credentials.

🗂 Creating a Database

🆕 Create a new database

In the left column of phpMyAdmin → click Create database → give it a name.

📊 Import data from Excel

Convert Excel to CSV.

Upload it to phpMyAdmin → set delimiter (; instead of ,) → click Import.

💡 Tip: Make sure column names in CSV match your database fields.

🐍 Installing Django

🔍 Check Python version

python --version


⚡ Create virtual environment

python -m venv venv


🚀 Activate virtual environment

On Windows:

venv\Scripts\activate


On Linux/macOS:

source venv/bin/activate


📦 Install Django

pip install django


⚠ Make sure it’s pip not pipe.

📁 Create Django project

django-admin startproject myproject


🏃 Run Django development server

cd myproject
python manage.py runserver


Open the URL it provides (e.g., http://127.0.0.1:8000)

You will see a rocket 🚀 icon indicating the server is running.

🛠 Create Django app

python manage.py startapp my_app


This will create a folder my_app inside myproject.

💻 Open project in VS Code

code .


Opens both myproject and my_app in VS Code.

### Για την δημιουργία φόρμας:

Εγκατάσταση PostgreSQL από το chat να το ρωτήσω, ανοίγεις το αρχείο, ναι σε όλα, αφήνεις επιλεγμένα αυτά που σου έχει

Διάλεξε φάκελο εγκατάστασης 

βάζεις pass word 

αφήνεις το Port 5432

αφήνεις default 

next next install finish 

Στο πλαίσιο: PostgreSQL 18(x64) on Port 5432

next cancel close 

start pgAdmin servers pass word 

Databases δεξί κλικ create database 

σύνδεση django με PostgreSQL 

στο ίδιο cmd (εκεί που υπάρχει δλδ το manage.py) γράψε: 

pipe install psycopg2 -binary , αν είναι οκ συνεχίζουμε 

τα στοιχεία της βάσης:

Database name: mydata

user: postgres

Pass word: τον κωδικό που έβαλες κατά τη. εγκατάσταση του PostgreSQL 

host: Localhost 

Port: 5432

άνοιξε το αρχείο settings.py

στο σημείο Database={.....}

αντικατέστησε από το σημείο 'Name': 'mydata', 

όταν τελειώσεις με τα παραπάνω, στο ίδιο cmd τρέξε: 

python manage.py migrate για να δημιουργήσει tables στη βάση 

Στο cmd: python manage.py startapp excel_data με την οποία δημιουργείται ο φάκελος "excel_data"

στα settings βρες το INSTALLED_APPS και πρόσθεσε τη γραμμή 'mydata', στο τέλος και αποθήκευσε

Στον φάκελο αυτόν, ώρες το models.py και άνοιξε το στο visual και αντικατέστησε το με τον κώδικα .... και save 

Στο cmd python manage.py makemigrations

python manage.py migrate 

Όποτε θα εμφανίζονται τα εξής:

Είναι παντού οκ 

Servers Databases mydata shima public tables βλέπεις όλους τους πίνακες 

τρέχει ο django server χωρίς να κάνει λάθη 












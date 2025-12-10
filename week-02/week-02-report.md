Combining a Web Server with PHP and MySQL

Last week I did MySQL and Web Server. So this week we will do PHP in combination with the two above.

For PHP, the following steps apply: ✅
In the Apache folder, specifically in httpd, replace AddType with AddHandler on the second-to-last line

Then, optionally, go to Start, open services.msc, find Apache24, and restart it

Go to the Apache path, then to htdocs, where we create a new file named info.php containing the code

Finally, after entering localhost, information related to PHP is displayed

Σύνδεση server με MySql kai me php

κατέβασμα phpmyadmin -all languages το βάζουμε εκεί C: Apache24 htdocs phpmyadmin εξαγωγή όλων των στοιχείων σε αυτόν τον φάκελο

Στο path αυτό, κάνεις αντιγραφή το config.sample.inc.php και το μετονομάζεις το καινούριο σε config.inc.php

ανοίγεις το καινούριο και στην γραμμή 16 προσθέτεις εναν τυχαίο κωδικό 32 χαρακτήρων

ανοίγεις το httpd.conf και προσθέτεις στο τέλος:

Alias phpmyadmin "C:\Apache24/htdocs\phpmyadmin"

<Directory "C:\Apache24\htdocs\phpmyadmin">

AllowOverride All

Requires all granted

and save

Στο cmd as admin: cd C:/Apache24/bin και μετά httpd -k start

Άνοιξε httpd:/localhost/phpmyadmin. Αν είναι εντάξει θα δεις την φόρμα login του phpmyadmin

user name, pass word

Δημιουργία βάσης δεδομένων

1)new αριστερή στήλη create database, δίνεις όνομα στο database

2)Μετατρέπουμε ένα excel με στοιχεία σε CSV για να γίνει import στη βάση δεδομένων

ανεβάζουμε το excel και αντί για , βάζουμε ; εκεί που το αναφέρει και import

Εγκατάσταση django

Στο cmd ως admin

python --version

python -m venv venv

venv\scripts\activate

pipe install django

django_admin startproject myproject

από εδώ και Κάτω θα πρέπει να είναι ενεργοποιημένο το venv να φαίνεται 

cd myproject

python manage.py runserver

μετά παίρνεις την ip που σου δίνει και εμφανίζει έναν πύραυλο

μετά πατάς python manage.py startapp my_app (δημιουργεί φάκελο μέσα στο my_project)

με την εντολή code . ανοίγει ο φάκελος my_app και ο my_project στο vs code

Για την δημιουργία φόρμας:

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












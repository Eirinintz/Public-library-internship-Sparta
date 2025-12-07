Η πρώτη εβδομάδα ξεκίνησε με στόχο την δημιουργία ενός web server ο οποίος θα εμφανίζει συγκεκριμένα μηνύματα σε web pages και θα τρέχει σε γλώσσες python και php. Αρχικά, τα βήματα για την εγκατάσταση των γλωσσών προγραμματισμού python & php, είναι τα παρακάτω:


## 1️⃣ Python

- Δημιουργία φακέλου με όνομα: "Project_Folder" στο path C:\
- Δημιουργία αρχείου στο notepad με όνομα: "app.py", όπου αποθηκεύεις τον αντίστοιχο κώδικα python που φαίνεται στον φάκελο "week-01" και επιλέγοντας "ολα τα αρχεία" αποθηκεύεις το αρχείο αυτό στον φάκελο "Project_Folder"
- Στον φακελο "Project_Folder", δημιουργείς καινούριο φάκελο με όνομα: "templates". Στον φάκελο "templates", με χρήση του notepad δημιουργείς ένα αρχείο με όνομα: "index.html" όπου αποθηεκύεις τον κώδικα που φαίνεται στον φάκελο "week-01", έχοντας επιλέξει "όλα τα αρχεία"
- Για την εγκατασταση του flask, ανοίγεις τον command prompt, όπου εισάγεις την εντολή: "install flask set FLASK_APP=app.py"
- Εφόσον είναι εγκατεστημένο στον υπολογιστή σου το Visual Studio Code (αν δεν υπάρχει, χρειάζεται να το εγκαταστήσεις), στα αριστερά στα "extensions" χρειάζεται να εγκαταστήσεις το "extension python"
- Ανοίγεις το αρχείο με τον κώδικα "app.py" και τρέχεις είτε στο terminal του VS code την εντολή: "python app.py" είτε στο cmd του υπολογιστή σου: "cd C:\Users..." εισάγοντας το path που δείχνει στον φάκελο και τρέχεις "python app.py"
-  Αν όλα έχουν πάει καλά, μετά το run, εμφανίζεται το κατάλληλο url: "http:..." το οποίο περνώντας το σε έναν browser εμφανίζονται τα μηνύματα "Hello!" "Welcome!" "This is a message."


## gia php

https://windows.php.net/download/  install php

δημιουργία φακελου PHP στο path C:\php, extract all files there


στον ίδιο φάκελο δημιουργείς αρχείο index.php all files με τον κώδικα php


extension php on visual code


στο cmd -> cd C:\... ekei pou einai o fakelos 

παιρνεις το localhost και το περνάς στον browser και εμφανιζει τα μηνύματα




## MySQLDB
για την αποθηκευση των δεδομένων των βιβλίων 

steps:
site: https://dev.mysql.com/downloads/installer/   install last


open file, select: full, steps: next, execute in order to be installed products


create your account and finish the installation


## Apache, without XAMPP and WAMP

Steps for web server:

site: https://www.apachelounge.com/download/ and install the appropriate one


new file -> path C:\Apache24  and extract all files from download there


sto path: C:\Apache24\conf\httpd.conf open last file, make sure the line: Define SRVROOT "/Apache24" deixnei: Define SRVROOT "c:/Apache24" and make sure that the lines below are exist without #:

  LoadModule php_module "c:/php/php8apache2_4.dll"

  AddType application/x-httpd-php .php


  PHPIniDir "C:/php"

and save the file



cmd as admin -> write: 

cd C:\Apache24\bin
httpd.exe -k install, service is installed



in the same terminal write: httpd.exe -k start


browser -> give localhost and then if it is ok appears the message: "It works!"

(php and Apache24 in the same path C:\)




## ρυθμιση php 

sto path C:\Apache24\conf to file httpd antikatastasi sthn proteleytaia grammi poy prosthesame prin toy AddTupe me AddHandler



(proairetika) -> start -> Services.msc -> Apache24 -> restart


sto C:\Apache24\htdocs new file me onoma info.php  apo notepad o code:



<? php
phpinfo();
?>



save as info.php all files



if it is ok, then open browser -> http://.../info.php -> and appears php informations



Τέλος, πέρα από το κομμάτι της πληροφορικής, εργαστήκαμε σε excel με στόχο την καταμέτρηση των βιβλίων και την καλύτερη οργάνωση-ταξινόμηση των βιβλίων της βιβλιθήκης και RFID για  την γρήγορη αναζήτηση όποιου βιβλίου. Τι είναι το RFID?

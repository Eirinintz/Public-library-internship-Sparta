# Week 1  💪⌛🗓️

## Creating a Web Server and displaying messages on a website using Python and PHP and Combining a Web Server with PHP and MySQL 📚

### 🎯 Creating a Web Server and displaying messages on a website using Python and PHP

#### For Python, the following steps apply: ✅

1) Create a folder named Project_Folder on the local disk

2) Create a file named ***app.py*** inside this folder with the code

3) Create a folder named **templates** inside the same folder, and within it create a file with the code ***index.html***

4) Download the Visual Studio Code application, install the Python extension, and add the code in a file named ***app.py***

5) Install Flask in the Command Prompt, then run:

```
set FLASK_APP=app.py

```

,and finally

```
python app.py
```

6) Run the code in Visual Studio Code and get the URL/path that appears in the Visual Studio Code Command Prompt

7) Paste it into a Web Page, and the messages from the code will be displayed

#### For Php, the following steps apply: ✅

1) Download PHP, extract the file, and place a new folder named **php** on the local disk containing all the contents of the zip file

2) In the same folder, add a file named ***index.php*** containing the code

3) Install a PHP extension in Visual Studio Code and run the code

4) In the Command Prompt, change the directory to the folder path and then run:

```
php -S localhost:8080
```

5) Display the URL/path, paste it into a Web Page, and the messages will be shown

---

### 🎯 Combining a Web Server with MySQL and PHP

#### For MySQL, the following steps apply: ✅

1) Download the latest version of MySQL and install it

2) Create an account and finish the installation

#### For Web server, the following steps apply: ✅

1) Download an Apache Server without XAMPP or WAMP, extract the folder, and place its contents in the correct path, specifically `C:\Apache24` on the local disk

2) In this folder, open the **httpd.conf** file to make some changes

3) We made sure that the line `Define SRVROOT /Apache24` is set to `Define SRVROOT c:/Apache24`

4) And finally, we added the following lines if they do not already exist:

```
LoadModule php_module c:/php/php8apache2_4.dll
AddType application/x-httpd-php .php
PHPIniDir C:/php
```,

and then we save the file

5) Open the Command Prompt as Administrator and set the correct path to show the following:

```
httpd cd C:\Apache24\bin
```, and then

```
httpd.exe -k install
```,

so, apache has been installed

6) In the same Command Prompt, enter:

```
httpd.exe -k start
```,

to start it

7) Apache must be in the same path as the PHP folder to run **httpd.exe**, and finally the message *It works* appears on a Web Page at localhost

#### For PHP, the following steps apply: ✅

1) In the Apache folder, specifically in httpd, replace AddType with AddHandler on the second-to-last line

2) Then, optionally, go to Start, open services.msc, find Apache24, and restart it

3) Go to the Apache path, then to htdocs, where we create a new file named info.php containing the code

4) Finally, after entering localhost, information related to PHP is displayed 

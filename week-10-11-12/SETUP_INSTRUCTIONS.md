# 📚 Internship Project - Books Database (Laravel)

## Μετατροπή από Django σε Laravel

---

## 🚀 ΟΔΗΓΙΕΣ ΕΓΚΑΤΑΣΤΑΣΗΣ - ΒΗΜΑ ΠΡΟΣ ΒΗΜΑ

### ✅ ΒΗΜΑ 1: Ρύθμιση Βάσης Δεδομένων

1. Άνοιξε το **phpMyAdmin** στο browser σου (συνήθως: `http://localhost/phpmyadmin`)

2. Βεβαιώσου ότι έχεις ήδη δημιουργήσει τη βάση `internship_project`
   - Αν όχι, δημιούργησε την: **New** → Όνομα: `internship_project` → **Create**

3. Πήγαινε στη βάση `internship_project` και πάτα την καρτέλα **SQL**

4. Άνοιξε το αρχείο `database_setup.sql` που βρίσκεται στο root folder του project

5. Αντίγραψε ΟΛΟ το περιεχόμενο και κάνε paste στο SQL tab του phpMyAdmin

6. Πάτα **Go** για να εκτελεστεί το script

7. ✅ Θα δεις μήνυμα επιτυχίας και οι πίνακες θα δημιουργηθούν!

---

### ✅ ΒΗΜΑ 2: Ρύθμιση .env αρχείου

1. Άνοιξε το αρχείο `.env` στο root folder του Laravel project

2. Βρες τη γραμμή:
   ```
   DB_PASSWORD=YOUR_PASSWORD_HERE
   ```

3. Αντικατάστησε το `YOUR_PASSWORD_HERE` με τον κωδικό της MySQL σου
   - Αν δεν έχεις κωδικό (default), άφησε το κενό:
     ```
     DB_PASSWORD=
     ```
   - Αν έχεις κωδικό, βάλε τον:
     ```
     DB_PASSWORD=your_mysql_password
     ```

4. Αποθήκευσε το αρχείο

---

### ✅ ΒΗΜΑ 3: Εγκατάσταση Dependencies

Άνοιξε **Command Prompt** ή **PowerShell** στο folder του project και τρέξε:

```bash
composer install
```

Αυτό θα εγκαταστήσει όλα τα Laravel packages που χρειάζονται.

---

### ✅ ΒΗΜΑ 4: Εκτέλεση του Laravel Server

Στο ίδιο Command Prompt/PowerShell, τρέξε:

```bash
php artisan serve
```

Θα δεις κάτι σαν:
```
Laravel development server started: http://127.0.0.1:8000
```

---

### ✅ ΒΗΜΑ 5: Άνοιγμα της Εφαρμογής

Άνοιξε τον browser σου και πήγαινε στο:
```
http://127.0.0.1:8000
```

🎉 **Το Laravel project θα είναι έτοιμο!**

---

## 📋 ΤΙ ΕΧΕΙ ΟΛΟΚΛΗΡΩΘΕΙ ΜΕΧΡΙ ΣΤΙΓΜΗΣ

### ✅ Ολοκληρώθηκε:
- [x] Δημιουργία βάσης δεδομένων και πινάκων
- [x] Migration files για persons, upload_logs
- [x] Person Model με όλα τα πεδία από το Django
- [x] UploadLog Model
- [x] Ρύθμιση .env αρχείου

### 🔄 Επόμενα Βήματα:
- [ ] Controllers (PersonController, UploadController, AuthController)
- [ ] Views (Blade templates)
- [ ] Routes configuration
- [ ] Authentication system
- [ ] Excel upload functionality
- [ ] Search & Filter functionality
- [ ] Pagination
- [ ] Autocomplete fields
- [ ] Print functionality

---

## 📊 ΔΟΜΗ ΒΑΣΗΣ ΔΕΔΟΜΕΝΩΝ

### Πίνακας: `persons`
Κύριος πίνακας με τα βιβλία της βιβλιοθήκης

| Πεδίο | Τύπος | Περιγραφή |
|-------|-------|-----------|
| ari8mosEisagoghs | int (PK) | Αριθμός Εισαγωγής |
| hmeromhnia_eis | varchar(200) | Ημερομηνία Εισαγωγής |
| syggrafeas | varchar(200) | Συγγραφέας |
| koha | varchar(200) | Koha (auto-generated) |
| titlos | varchar(200) | Τίτλος |
| ekdoths | varchar(200) | Εκδότης |
| ekdosh | varchar(200) | Έκδοση |
| etosEkdoshs | varchar(20) | Έτος Έκδοσης |
| toposEkdoshs | varchar(200) | Τόπος Έκδοσης |
| sxhma | varchar(200) | Σχήμα |
| selides | varchar(50) | Σελίδες |
| tomos | varchar(50) | Τόμος |
| troposPromPar | varchar(200) | Τρόπος Προμήθειας |
| ISBN | varchar(50) | ISBN |
| sthlh1 | varchar(200) | Στήλη 1 |
| sthlh2 | varchar(200) | Στήλη 2 |

### Πίνακας: `upload_logs`
Ιστορικό μεταφορτώσεων Excel

| Πεδίο | Τύπος | Περιγραφή |
|-------|-------|-----------|
| id | bigint (PK) | Auto-increment ID |
| user_id | bigint (FK) | Χρήστης που έκανε upload |
| filename | varchar(255) | Όνομα αρχείου |
| rows_added | int | Εγγραφές που προστέθηκαν |
| rows_updated | int | Εγγραφές που ενημερώθηκαν |
| created_at | timestamp | Ημερομηνία upload |

---

## 🛠️ ΧΡΗΣΙΜΕΣ ΕΝΤΟΛΕΣ LARAVEL

```bash
# Εκκίνηση development server
php artisan serve

# Εκτέλεση migrations (αν χρειαστεί αργότερα)
php artisan migrate

# Δημιουργία νέου controller
php artisan make:controller ControllerName

# Καθαρισμός cache
php artisan cache:clear
php artisan config:clear
php artisan route:clear

# Δημιουργία symbolic link για storage
php artisan storage:link
```

---

## 📝 ΣΗΜΕΙΩΣΕΙΣ

- Το project χρησιμοποιεί MySQL με το Laravel Eloquent ORM
- Όλα τα πεδία είναι nullable εκτός από το primary key (ari8mosEisagoghs)
- Τα timestamps (created_at, updated_at) προστίθενται αυτόματα από το Laravel
- Το authentication θα υλοποιηθεί με το Laravel Breeze ή UI package

---

## 📞 ΕΠΟΜΕΝΑ ΒΗΜΑΤΑ

Μόλις ολοκληρώσεις τα παραπάνω βήματα, πες μου και θα συνεχίσουμε με:
1. Δημιουργία Controllers
2. Δημιουργία Views (Blade templates)
3. Routes configuration
4. Authentication system

---

**Ημερομηνία:** 12 Φεβρουαρίου 2026  
**Έκδοση Laravel:** 11.x  
**Έκδοση PHP:** 8.5.0

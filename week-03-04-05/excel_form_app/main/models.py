from django.db import models  # Import Django models
from django.contrib.auth.models import User  # Import Django's built-in User model


# Model representing a book/person entry
class Person(models.Model):
    ari8mosEisagoghs = models.CharField(unique=True, primary_key=True, max_length=200, blank=True)  # Unique entry number
    hmeromhnia_eis = models.CharField(max_length=200, null=True, blank=True)  # Entry date
    syggrafeas = models.CharField(max_length=200, null=True, blank=True)  # Author
    koha = models.CharField(max_length=200, null=True, blank=True)  # KOHA author format
    titlos = models.CharField(max_length=200, null=True, blank=True)  # Title
    ekdoths = models.CharField(max_length=200, null=True, blank=True)  # Publisher
    ekdosh = models.CharField(max_length=200, null=True, blank=True)  # Edition
    etosEkdoshs = models.CharField(max_length=20, null=True, blank=True)  # Year of publication
    toposEkdoshs = models.CharField(max_length=200, null=True, blank=True)  # Place of publication
    sxhma = models.CharField(max_length=200, null=True, blank=True)  # Shape/format
    selides = models.CharField(max_length=50, null=True, blank=True)  # Number of pages
    tomos = models.CharField(max_length=50, null=True, blank=True)  # Volume
    troposPromPar = models.CharField(max_length=200, null=True, blank=True)  # Supply/remarks
    ISBN = models.CharField(max_length=50, null=True, blank=True)  # ISBN number
    sthlh1 = models.CharField(max_length=200, null=True, blank=True)  # Column 1 (custom)
    sthlh2 = models.CharField(max_length=200, null=True, blank=True)  # Column 2 (custom)

    def __str__(self):
        return self.ari8mosEisagoghs  # Display entry number as string representation


# Model for tracking Excel uploads
class UploadLog(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="uploads"  # Allows reverse lookup: user.uploads.all()
    )
    uploaded_at = models.DateTimeField(auto_now_add=True)  # Timestamp of upload
    filename = models.CharField(max_length=255)  # Name of uploaded file
    rows_added = models.PositiveIntegerField(default=0)  # Number of new rows added
    rows_updated = models.PositiveIntegerField(default=0)  # Number of rows updated

    def __str__(self):
        # Show filename, user, and timestamp in admin or console
        return f"{self.filename} by {self.user.username} on {self.uploaded_at}"

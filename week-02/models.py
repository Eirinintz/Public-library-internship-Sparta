from django.db import models  # Django ORM module for database models
from django.contrib.auth.models import User  # Built-in Django user model

# Model to store information about a person/book entry
class Person(models.Model):
    ari8mosEisagoghs = models.CharField(unique=True, primary_key=True, max_length=200, blank=True)  # Unique identifier
    hmeromhnia_eis = models.CharField(max_length=200, null=True, blank=True)  # Entry date
    syggrafeas = models.CharField(max_length=200, null=True, blank=True)  # Author
    koha = models.CharField(max_length=200, null=True, blank=True)  # Possibly "subject" or category
    titlos = models.CharField(max_length=200, null=True, blank=True)  # Title
    ekdoths = models.CharField(max_length=200, null=True, blank=True)  # Publisher
    ekdosh = models.CharField(max_length=200, null=True, blank=True)  # Edition
    etosEkdoshs = models.CharField(max_length=20, null=True, blank=True)  # Year of publication
    toposEkdoshs = models.CharField(max_length=200, null=True, blank=True)  # Place of publication
    sxhma = models.CharField(max_length=200, null=True, blank=True)  # Format
    selides = models.CharField(max_length=50, null=True, blank=True)  # Number of pages
    tomos = models.CharField(max_length=50, null=True, blank=True)  # Volume
    troposPromPar = models.CharField(max_length=200, null=True, blank=True)  # Supply/Distribution method
    ISBN = models.CharField(max_length=50, null=True, blank=True)  # ISBN
    sthlh1 = models.CharField(max_length=200, null=True, blank=True)  # Extra column 1
    sthlh2 = models.CharField(max_length=200, null=True, blank=True)  # Extra column 2

    def __str__(self):
        return self.name  # Display name (this will throw an error because `name` field does not exist)

# Model to log CSV or file uploads
class UploadLog(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,  # If the user is deleted, also delete their uploads
        related_name="uploads"  # Reverse relation: user.uploads.all()
    )
    uploaded_at = models.DateTimeField(auto_now_add=True)  # Automatically set the upload time
    filename = models.CharField(max_length=255)  # Name of the uploaded file
    rows_added = models.PositiveIntegerField(default=0)  # Number of rows added
    rows_updated = models.PositiveIntegerField(default=0)  # Number of rows updated

    def __str__(self):
        return f"{self.filename} by {self.user.username} on {self.uploaded_at}"  # Human-readable string

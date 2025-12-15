from django.db import models

# Book model representing a book record in the database
class Book(models.Model):
    # Entry number of the book
    entry_number = models.IntegerField()

    # Date when the book was entered
    entry_date = models.DateField()

    # Author of the book
    author = models.CharField(max_length=255)

    # Alternative author name (e.g. Koha system), optional
    koha_author = models.CharField(max_length=255, blank=True, null=True)

    # Title of the book
    title = models.CharField(max_length=255)

    # Publisher name, optional
    publisher = models.CharField(max_length=255, blank=True, null=True)

    # Edition information, optional
    edition = models.CharField(max_length=255, blank=True, null=True)

    # Year of publication, optional
    publish_year = models.IntegerField(blank=True, null=True)

    # Place of publication, optional
    publish_place = models.CharField(max_length=255, blank=True, null=True)

    # Physical shape or format of the book, optional
    shape = models.CharField(max_length=255, blank=True, null=True)

    # Number of pages, optional
    pages = models.CharField(max_length=50, blank=True, null=True)

    # Volume information, optional
    volume = models.CharField(max_length=50, blank=True, null=True)

    # Additional notes, optional
    notes = models.TextField(blank=True, null=True)

    # ISBN number, optional
    isbn = models.CharField(max_length=50, blank=True, null=True)

    # Extra custom field, optional
    column1 = models.CharField(max_length=255, blank=True, null=True)

    # Extra custom field, optional
    column2 = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        # String representation of the model
        return self.title

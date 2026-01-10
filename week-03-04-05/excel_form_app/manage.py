#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""

import os
import sys

def main():
    """Run administrative tasks."""
    # Ορίζουμε την προεπιλεγμένη ρύθμιση για το Django project
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'excel_form_app.settings')

    try:
        # Εισάγουμε την συνάρτηση που εκτελεί εντολές από τη γραμμή εντολών
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # Αν δεν βρεθεί η Django, εμφανίζεται κατατοπιστικό μήνυμα
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    # Εκτέλεση εντολών Django που δίνονται από τη γραμμή εντολών
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    # Κλήση της κύριας συνάρτησης
    main()

"""
WSGI config for excel_form_app project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

import os  # Provides access to environment variables and OS-level functionality

from django.core.wsgi import get_wsgi_application  # Imports Django's WSGI application factory

# Set the default Django settings module for the WSGI application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'excel_form_app.settings')

# Create the WSGI application callable used by WSGI servers
application = get_wsgi_application()

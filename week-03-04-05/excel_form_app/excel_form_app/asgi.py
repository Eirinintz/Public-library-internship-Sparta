"""
ASGI config for excel_form_app project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/asgi/
"""

import os  # Provides functions to interact with the operating system

from django.core.asgi import get_asgi_application  # Imports Django's ASGI application factory

# Set the default Django settings module for the ASGI application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'excel_form_app.settings')

# Create the ASGI application callable used by ASGI servers
application = get_asgi_application()

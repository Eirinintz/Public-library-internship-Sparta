from django.contrib import admin  # Import Django admin site
from django.urls import path, include  # Import path for URL routing and include for app URLs

# Define the URL patterns for the project
urlpatterns = [
    # Admin panel URL
    path('admin/', admin.site.urls),

    # Include URLs from the "main" application
    path('', include('main.urls')),  # include your app URLs
]

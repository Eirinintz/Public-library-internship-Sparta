from django.contrib import admin  # Import Django admin
from django.urls import path, include  # Import path and include for URL routing
from . import views  # Import views from current app
from .views import upload_excel, show_people, SignUpView, autocomplete_title, autocomplete_ekdoths  # Import specific views


urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('signup/', SignUpView.as_view(), name='signup'),  # User registration page
    path('accounts/', include('django.contrib.auth.urls')),  # Login, logout, password management URLs
    path('people/', views.show_people, name='show_people'),  # Display all people/records
    path('upload/', views.upload_excel, name='upload_excel'),  # Upload Excel file
    path('duplicates/', views.resolve_duplicates, name='resolve_duplicates'),  # Resolve duplicates page
    path('duplicates/handle/', views.handle_duplicate, name='handle_duplicate'),  # Handle single duplicate actions (edit/skip)
    path('person/edit/<str:pk>/', views.edit_person, name='edit_person'),  # Edit a specific person's record by primary key
    path('skip-all-duplicates/', views.skip_all_duplicates, name='skip_all_duplicates'),  # Skip all duplicates at once
    path('add-person/', views.add_person, name='add_person'),  # Manually add a person/book record
    path('ajax/autocomplete/title/', views.autocomplete_title, name='autocomplete_title'),  # AJAX endpoint for title autocomplete
    path('ajax/autocomplete/ekdoths/', views.autocomplete_ekdoths, name='autocomplete_ekdoths'),  # AJAX endpoint for publisher autocomplete
]

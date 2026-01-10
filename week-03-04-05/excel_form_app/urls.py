from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

# Λίστα URL patterns που δρομολογούν κάθε αίτημα HTTP στο σωστό view
urlpatterns = [
    # 🔹 Admin panel
    path("admin/", admin.site.urls),
    # ➤ Όλα τα URLs για authentication (login, logout, password_change, κλπ.)
    path("accounts/", include("django.contrib.auth.urls")),
    
    # 🔹 Όλα τα URLs της εφαρμογής 'main' (π.χ. /upload/, /people/, /add-person/)
    path('', include('main.urls')),

    # 🔹 Αρχική σελίδα
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
]

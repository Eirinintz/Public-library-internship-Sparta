from django.urls import path
from .views import upload_excel, show_people

urlpatterns = [
    path('people/', show_people, name='people'),
    path('upload/', upload_excel, name='upload_excel'),
]

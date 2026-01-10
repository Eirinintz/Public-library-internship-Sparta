from django.contrib import admin
from .models import UploadLog  # Import the UploadLog model

# Register the UploadLog model in the Django admin
@admin.register(UploadLog)
class UploadLogAdmin(admin.ModelAdmin):
    # Columns to display in the admin list view
    list_display = ("filename", "user", "uploaded_at", "rows_added", "rows_updated")
    
    # Filters to use in the admin sidebar
    list_filter = ("user", "uploaded_at")

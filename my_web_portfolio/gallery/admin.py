from django.contrib import admin
from .models import GalleryImage

@admin.register(GalleryImage)
class YourModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image')  # Fields to display in the admin list view
    search_fields = ('title', 'description')  # Fields to search in the admin interface
    list_filter = ('title', 'description')  # Fields for filtering in the admin interface

from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('sku', 'description', 'qtyperpcs','bccs','bcib','bcpcs')  # Fields to display in the admin list view
    search_fields = ('sku', 'description')  # Fields to search in the admin interface
    list_filter = ('sku', 'description')  # Fields for filtering in the admin interface


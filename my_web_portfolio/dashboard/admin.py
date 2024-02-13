from django.contrib import admin
from .models import Product, Valuation, Promo

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('sku', 'description', 'qtyperpcs','bccs','bcib','bcpcs')  # Fields to display in the admin list view
    search_fields = ('sku', 'description')  # Fields to search in the admin interface
    list_filter = ('sku', 'description')  # Fields for filtering in the admin interface

@admin.register(Promo)
class PromoAdmin(admin.ModelAdmin):
    list_display = ('sku', 'child_sku','mech_per_pcs')  # Fields to display in the admin list view
    search_fields = ('sku',)  # Fields to search in the admin interface
    list_filter = ('sku',)  # Fields for filtering in the admin interface

@admin.register(Valuation)
class ValuationAdmin(admin.ModelAdmin):
    list_display = ('sku', 'description', 'cs','ib','pcs')  # Fields to display in the admin list view
    search_fields = ('sku', 'description')  # Fields to search in the admin interface
    list_filter = ('sku', 'description')  # Fields for filtering in the admin interface

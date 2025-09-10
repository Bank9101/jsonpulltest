from django.contrib import admin
from .models import OTOPProduct

# Register your models here.

@admin.register(OTOPProduct)
class OTOPProductAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'shop_name', 'district', 'province', 'has_coordinates']
    list_filter = ['province', 'district', 'local_admin']
    search_fields = ['product_name', 'shop_name', 'address', 'province', 'district']
    list_per_page = 50
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Product Information', {
            'fields': ('product_name', 'shop_name')
        }),
        ('Location Details', {
            'fields': ('local_admin', 'district', 'province', 'address', 'phone')
        }),
        ('Coordinates', {
            'fields': ('latitude', 'longitude')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        })
    )

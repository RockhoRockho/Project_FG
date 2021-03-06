
from django.contrib import admin

from .models import Product

class ProductAdmin(admin.ModelAdmin):
    
    list_display = ('product', 'name', 'price', 'category', 'seller', 'reg_date')
    list_filter = ('seller',)
    icon_name = 'shopping_cart'
    search_fields = ['product', 'name', 'category', 'seller']

admin.site.register(Product, ProductAdmin)
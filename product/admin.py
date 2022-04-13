from django.contrib import admin

from .models import Product

class ProductAdmin(admin.ModelAdmin):
    
    list_display = ('product', 'name', 'price', 'category', 'seller', 'reg_date')
    list_filter = ('reg_date',)
admin.site.register(Product, ProductAdmin)





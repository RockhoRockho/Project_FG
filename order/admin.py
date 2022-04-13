from django.contrib import admin

from .models import Order, Order_items, Cart

admin.site.register(Order)
admin.site.register(Order_items)
admin.site.register(Cart)

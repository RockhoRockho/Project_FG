from django.contrib import admin

from .models import Order, Order_items, Cart, TempOrder
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'date', 'delivery_address', 'receiver_name')

class Order_itemsAdmin(admin.ModelAdmin):
    list_display = ('member','product','price', 'quantity')
class CartAdmin(admin.ModelAdmin):
    list_display = ('member', 'product', 'quantity')
class TempOrderAdmin(admin.ModelAdmin):
    list_display = ('member', 'product', 'price', 'quantity')

admin.site.register(Order, OrderAdmin)
admin.site.register(Order_items, Order_itemsAdmin)
admin.site.register(Cart,CartAdmin)
admin.site.register(TempOrder, TempOrderAdmin)

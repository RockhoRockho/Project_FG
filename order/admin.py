from django.contrib import admin

from .models import Order, Order_items, Cart, TempOrder
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'date', 'delivery_address', 'receiver_name')
    icon_name = 'content_paste'
    search_fields = ['order_id', 'receiver_name']

class Order_itemsAdmin(admin.ModelAdmin):
    list_display = ('member','product','price', 'quantity')
    icon_name = 'subject'
    search_fields = ['member', 'product']

class CartAdmin(admin.ModelAdmin):
    list_display = ('member', 'product', 'quantity')
    icon_name = 'add_shopping_cart'
    search_fields = ['member', 'product']

class TempOrderAdmin(admin.ModelAdmin):
    list_display = ('member', 'product', 'price', 'quantity')
    icon_name = 'reply_all'
    search_fields = ['member', 'product']

admin.site.register(Order, OrderAdmin)
admin.site.register(Order_items, Order_itemsAdmin)
admin.site.register(Cart,CartAdmin)
admin.site.register(TempOrder, TempOrderAdmin)

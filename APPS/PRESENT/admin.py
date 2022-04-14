from django.contrib import admin

from .models import Present

class PresentAdmin(admin.ModelAdmin):
    list_display = ('member', 'product', 'receiver_name', 'quantity',)
    list_filter = ('id',)
    icon_name = 'redeem'
    search_fields = ['member', 'product', 'receiver_name']

admin.site.register(Present, PresentAdmin)

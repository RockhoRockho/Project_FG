from django.contrib import admin

from .models import Present

class PresentAdmin(admin.ModelAdmin):
    list_display = ('product', 'receiver_name', 'quantity',)
    list_filter = ('id',)
    icon_name = 'redeem'
admin.site.register(Present, PresentAdmin)






from django.contrib import admin

from .models import Pick

class PickAdmin(admin.ModelAdmin):
    list_display = ('member', 'product', 'comment')
    icon_name = 'favorite'
admin.site.register(Pick, PickAdmin)

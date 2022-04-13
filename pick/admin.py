from django.contrib import admin

from .models import Pick

class PickAdmin(admin.ModelAdmin):
    list_display = ('member', 'product', 'comment')

admin.site.register(Pick, PickAdmin)

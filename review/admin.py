from django.contrib import admin

from .models import Review

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('member', 'order_items', 'reg_date')
    list_filter = ('reg_date',)
    icon_name = 'create'
    
admin.site.register(Review, ReviewAdmin)

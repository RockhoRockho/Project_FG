from django.contrib import admin

from .models import Review

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('member', 'order_items', 'reg_date')
    list_filter = ('reg_date',)

admin.site.register(Review, ReviewAdmin)
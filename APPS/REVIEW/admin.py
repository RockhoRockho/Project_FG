from django.contrib import admin

from APPS.REVIEW.models import Review

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('member', 'product', 'reg_date')
    list_filter = ('reg_date',)
    icon_name = 'create'
    search_fields = ['member', 'order_items']


admin.site.register(Review, ReviewAdmin)
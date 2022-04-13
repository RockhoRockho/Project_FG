from django.contrib import admin

from .models import Service
class ServiceAdmin(admin.ModelAdmin):
    
    list_display = ('member', 'title', 'content', 'reg_date')
    list_filter = ('reg_date',)
    icon_name = 'report'
admin.site.register(Service, ServiceAdmin)


admin.site.site_header = "관리자 페이지"





from django.contrib import admin
from .models import Member

class MemberAdmin(admin.ModelAdmin):
    list_display = ('memberid', 'username', 'pw', 'name', 'gender', 'email', 'phoneNum')
    icon_name = 'person'
    search_fields = ['memberid', 'username', 'name']
admin.site.register(Member)
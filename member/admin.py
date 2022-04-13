from django.contrib import admin
from .models import Member

class MemberAdmin(admin.ModelAdmin):
    list_display = ('memberid', 'username', 'pw', 'name', 'gender', 'email', 'phoneNum')

admin.site.register(Member)


from django.contrib import admin

from .models import Member, Address
class MemberAdmin(admin.ModelAdmin):
    list_display = ('memberid', 'username', 'pw', 'name', 'gender', 'email', 'phoneNum')

class AdressAdmin(admin.ModelAdmin):
    list_display = ('post_num', 'address', 'address_detail', 'member')

admin.site.register(Member)
admin.site.register(Address)


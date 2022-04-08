from django.urls import path
from Leyhara import views;

app_name = "Leyhara"

urlpatterns = [
    path("main/", views.main, name='main'),
    path("login/check/", views.login_check, name='login_check'),
    path("member/check/", views.member_check, name='member_check'),
    path("member/info/", views.member_info, name='member_info'),
    path("register/", views.register, name='reg'),
    path("register/personal/", views.register_personal, name='reg_personal'),
]
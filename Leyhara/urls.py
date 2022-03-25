from django.urls import path
from Leyhara import views;

app_name = "Leyhara"

urlpatterns = [
    path("register/", views.register, name='reg'),
    path("register/personal/", views.register_personal, name='reg_personal'),
]
from django.urls import path
from present import views

urlpatterns = [
    path('present/list/', views.present_list, name='present_list'),
    path('present/send/', views.present_send, name='present_send'),
]

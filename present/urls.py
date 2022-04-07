from django.urls import path
from present import views

urlpatterns = [
    path('present/list/<int:member_pk>/', views.present_list, name='present_list'),
    path('present/send/<int:member_pk>/', views.present_send, name='present_send'),
]

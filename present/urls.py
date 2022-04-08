from django.urls import path
from present import views

urlpatterns = [
    path('list/', views.present_list, name='present_list'),
    path('send/', views.present_send, name='present_send'),
]

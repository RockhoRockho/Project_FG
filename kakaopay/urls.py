
from unicodedata import name
from django.contrib import admin
from django.urls import path
from kakaopay import views

urlpatterns = [
    path('', views.kakaopay, name='kakaopay'),
    path('approval', views.approval, name='approval'),
]

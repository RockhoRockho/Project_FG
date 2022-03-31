from unicodedata import name
from django.urls import path
from products import views

urlpatterns = [
    path('search/', views.search, name='search')
]

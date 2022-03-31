from django.urls import path
from Jun import views

urlpatterns = [
    path('product_best/', views.search_best, name='search_best'),
    path('product_category/', views.search_category, name='search_category'),
    path('cart/', views.cart, name='cart'),
]

from unicodedata import name
from django.urls import path
from products import views

urlpatterns = [
    path('search/', views.search, name='search'),
    path('order_by_rate/', views.order_by_rate, name='order_by_rate'),
    path('order_by_view/', views.order_by_view, name="order_by_view"),
    path('search_error/', views.search_error, name='search_error'),
    path('review/', views.review, name='review'),
]

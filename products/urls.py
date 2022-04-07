from unicodedata import name
from django.urls import path
from products import views

urlpatterns = [
    path('search/', views.search, name='search'),
    path('order_by_rate/', views.order_by_rate, name='order_by_rate'),
    path('order_by_view/', views.order_by_view, name="order_by_view"),
    path('search_error/', views.search_error, name='search_error'),
    path('review/', views.review, name='review'),
    path('reviewed/', views.reviewed, name='reviewed'),
    path('present_view/', views.present_view, name='present_view'),

    
    # path('kakaopay/', views.kakaopay, name="kakaopay"),
    # path('paySuccess/', views.paySuccess, name='paySuccess'),
    # path('address/', views.address, name='address'),
    path('naverLogin/', views.naverLogin, name = 'naverLogin'),
    path('naverCallback', views.naverCallback, name = 'naverCallback'),
]

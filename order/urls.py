from django.urls import path
from order import views

urlpatterns = [
    path('list/', views.order_list, name='order_list.'),
    path('detail/', views.order_detail, name='order_detail'),
    path('cart/', views.order_cart, name='order_cart'),
    path('purchase/', views.order_purchase, name='order_purchase'),
    path('purchase/success/', views.order_success, name='order_success'),
]   

from django.urls import path
from order import views

urlpatterns = [
    path('list/', views.order_list, name='order_list.html'),
    path('detail/', views.order_detail, name='order_detail.html'),
    path('cart/', views.order_cart, name='order_cart.html'),
    path('purchase/', views.order_purchase, name='order_purchase.html'),
    path('purchase/success/', views.order_success, name='order_success.html'),
]   

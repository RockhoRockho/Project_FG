from django.urls import path
from order import views

urlpatterns = [
    path('list/<int:member_pk>/', views.order_list, name='order_list.html'),
    path('detail/<int:member_pk>/', views.order_detail, name='order_detail.html'),
    path('cart/<int:member_pk>', views.order_cart, name='order_cart.html'),
    path('purchase/<int:member_pk>/', views.order_purchase, name='order_purchase.html'),
    path('purchase/success/<int:member_pk>/', views.order_success, name='order_success.html'),
]   

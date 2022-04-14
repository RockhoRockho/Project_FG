from django.urls import path
from APPS.ORDER import views

urlpatterns = [
    path('list/', views.order_list, name='order_list'),
    path('cart/', views.order_cart, name='order_cart'),
    path('purchase/cart/', views.cart_purchase, name='cart_purchase'),
    path('update/<int:product_id>/', views.cart_update, name='cart_update'),
    path('delete/<int:product_id>/', views.cart_delete, name='cart_delete'),
    path('purchase/pay/<int:product_id>/', views.order_purchase, name='order_purchase'),
    path('purchase/success/', views.order_success, name='order_success'),
    path('cancel/', views.order_cancel, name='order_cancel'),
    path('before_kakao/', views.before_kakao, name='before_kakao'),
    path('kakaopay/', views.kakaopay, name='kakaopay'),
    path('kakaopay/approval/', views.approval, name='approval'),
]   

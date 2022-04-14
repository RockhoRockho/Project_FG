from django.urls import path
from present import views

urlpatterns = [
    path('list/', views.present_list, name='present_list'),
    path('send/<int:product_id>/', views.present_send, name='present_send'),
    path('cancel/<int:product_id>/', views.present_cancel, name='present_cancel'),
    path('success/', views.present_success, name='present_success'),
    path('before_kakao_present/', views.before_kakao_present, name='before_kakao_present'),
    path('kakaopay/', views.present_kakaopay, name='present_kakaopay'),
    path('kakaopay/approval/', views.present_approval, name='present_approval'),
]

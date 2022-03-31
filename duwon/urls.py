from django.urls import path
from duwon import views

urlpatterns = [
    path('detail/', views.product_detail, name='product_detail'),
]

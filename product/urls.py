from django.urls import path
from product import views

urlpatterns = [
    path('search/<str:product_name>/<int:page_num>/', views.product_search, name='product_search'),
    path('search/lprice/<str:product_name>/<int:page_num>/', views.product_lprice, name='product_lprice'),
    path('search/view/<str:product_name>/<int:page_num>/', views.product_view, name="product_view"),
    path('search/error/<str:product_name>/', views.product_error, name='product_error'),
    path('best/', views.product_best, name='product_best'),
    path('category/<str:category>/', views.product_category, name='product_category'),
    path('detail/<int:product_id>/', views.product_detail, name='product_detail'),
    path('before_cart/<int:product_id>/', views.before_cart, name='before_cart'),
    path('before_pick/<int:product_id>/', views.before_pick, name='before_pick'),
    path('before_pay/<int:product_id>/', views.before_pay, name='before_pay'),
    path('before_present/<int:product_id>/', views.before_present, name='before_present'),
]

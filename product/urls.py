from django.urls import path
from product import views

urlpatterns = [
    path('search/<slug:product_name>/', views.product_search, name='product_search'),
    # path('search/rate/<slug:product_name>/', views.product_rate, name='product_rate'),
    # path('search/view/<slug:product_name>/', views.product_view, name="product_view"),
    # path('search/error/<slug:product_name>/', views.product_error, name='product_error'),
    path('best/', views.product_best, name='product_best'),
    # path('category/<slug:category>/', views.product_category, name='product_category'),
    # path('detail/<int:product_id>/', views.product_detail, name='product_detail'),
]

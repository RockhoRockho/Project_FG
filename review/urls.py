from django.urls import path
from review import views

urlpatterns = [
    path('', views.review, name='review'),
    path('update/<int:id>/', views.review_update, name='review_update'),
    path('detail/<int:id>/', views.review_detail, name='review_detail'),
    path('delete/', views.review_delete, name='review_delete'),
]

from django.urls import path
from APPS.REVIEW import views

urlpatterns = [
    path('', views.review, name='review'),
    path('update/<int:id>/', views.review_update, name='review_update'),
    path('delete/', views.review_delete, name='review_delete'),
]
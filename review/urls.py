from django.urls import path
from review import views

urlpatterns = [
    path('', views.review, name='review'),
    path('update/<int:id>/', views.review_update, name='review_update'),
    path('delete/<int:id>/', views.review_delete, name='review_delete'),
]

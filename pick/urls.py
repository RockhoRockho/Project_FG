from django.urls import path
from pick import views

urlpatterns = [
    path('', views.pick, name='pick'),
    path('update/<int:pk>/', views.pick_update, name='pick_update'),
    path('delete/', views.pick_delete, name='pick_delete'),
]

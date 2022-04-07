from django.urls import path
from pick import views

urlpatterns = [
    path('pick/<int:member_pk>/', views.pick, name='pick'),
]

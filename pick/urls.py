from django.urls import path
from pick import views

urlpatterns = [
    path('', views.pick, name='pick'),
]

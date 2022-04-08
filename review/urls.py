from django.urls import path
from review import views

urlpatterns = [
    path('', views.review, name='review'),
]

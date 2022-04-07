from django.urls import path
from review import views

urlpatterns = [
    path('<int:member_pk>/', views.review, name='review'),
]

from django.urls import path
from member import views

urlpatterns = [
    path('login/', views.member_login, name='member_login.html'),
    path('join/', views.member_join, name='member_join.html'),
    path('terms/', views.member_terms, name='member_terms.html'),
]

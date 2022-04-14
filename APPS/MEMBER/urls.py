from django.urls import path
from APPS.MEMBER import views

urlpatterns = [
    path('findusername/', views.member_findusername, name='member_findusername'),
    path('findpw/', views.member_findpw, name='member_findpw'),
    path('found/', views.member_found, name='member_found'),
    path('login/', views.member_login, name='member_login'),
    path('logout/', views.member_logout, name='member_logout'),
    path('join/', views.member_join, name='member_join'),
    path('terms/', views.member_terms, name='member_terms'),
    path('info/', views.member_info, name='member_info'),
    path('needlogin/', views.member_needlogin, name='member_needlogin'),
    path('terms/detail', views.member_terms_detail, name='member_terms_detail'),
]
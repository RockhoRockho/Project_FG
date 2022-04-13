from django.urls import path
from member import views

urlpatterns = [
    path('login/', views.member_login, name='member_login'),
    path('logout/', views.member_logout, name='member_logout'),
    path('join/', views.member_join, name='member_join'),
    path('terms/', views.member_terms, name='member_terms'),
    path('info/', views.member_info, name='member_info'),
    path('check/', views.member_check, name='member_check'),
    path('needlogin/', views.member_needlogin, name='member_needlogin'),
]

from django.urls import path
from service import views

urlpatterns = [
    path('<int:member_pk>/', views.question_main, name="question_main"),
    path('write/<int:member_pk>/', views.question, name="question_write"),
    path('Ok/<int:member_pk>/', views.questionOK, name="questionOK"),
    path('detail/<int:member_pk>/', views.question_detail, name="question_detail"),
    path('update/<int:member_pk>/', views.question_update, name="question_update"),
    path('answer/<int:member_pk>/', views.question_answer, name="question_answer"),
]

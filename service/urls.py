from django.urls import path
from service import views

urlpatterns = [
    path('', views.question_main, name="question_main"),
    path('write/', views.question_write, name="question_write"),
    path('Ok/', views.questionOK, name="questionOK"),
    path('detail/<int:id>/', views.question_detail, name="question_detail"),
    path('update/', views.question_update, name="question_update"),
    path('answer/', views.question_answer, name="question_answer"),
]

from django.urls import path
from APPS.SERVICE import views

urlpatterns = [
    path('', views.question_main, name="question_main"),
    path('write/', views.question_write, name="question_write"),
    path('Ok/', views.questionOK, name="questionOK"),
    path('detail/<int:id>/', views.question_detail, name="question_detail"),
    path('update/<int:id>', views.question_update, name="question_update"),
    path('delete/', views.question_delete, name="question_delete"),
    path('answer/', views.question_answer, name="question_answer"),
]
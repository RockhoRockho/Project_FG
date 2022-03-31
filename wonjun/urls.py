from unicodedata import name
from django.urls import path
from wonjun import views

urlpatterns = [
    path('login/', views.login, name="login"),
    path('agreement/', views.agreement, name="agreement"),
    path('join/', views.join, name="join"),
    path('question/', views.question, name="question"),
    path('questionOK/', views.questionOK, name="questionOK"),
    path('question_update/', views.question_update, name="question_update"),
    path('question_detail/', views.question_detail, name="question_detail"),
]

from multiprocessing import context
from django.shortcuts import render

# Create your views here.
def login(request):
    context={

    }
    return render(request, 'login1.html', context)

def agreement(request):
    return render(request, "agreement.html")

def join(request):
    return render(request, "join.html")

def question(request):
    return render(request, "question.html")

def questionOK(request):
    return render(request, "questionOK.html")

def question_update(request):
    return render(request, "question_update.html")

def question_detail(request):
    return render(request, "question_detail.html")

def question_main(request):
    context = {
        'range' : range(5),
    }
    return render(request, "question_main.html", context)

def question_answer(request):
    return render(request, "question_answer.html")
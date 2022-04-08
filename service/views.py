from django.shortcuts import render

def question_main(request):
    context = {
        'range' : range(5),
    }
    return render(request, "question_main.html", context)

def question_write(request):
    return render(request, "question_write.html")

def questionOK(request):
    return render(request, "questionOK.html")

def question_update(request):
    return render(request, "question_update.html")

def question_detail(request):
    return render(request, "question_detail.html")

def question_answer(request):
    return render(request, "question_answer.html")



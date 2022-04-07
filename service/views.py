from django.shortcuts import render

def question_main(request, member_pk):
    context = {
        'range' : range(5),
    }
    return render(request, "question_main.html", context)

def question_write(request, member_pk):
    return render(request, "question_write.html")

def questionOK(request, member_pk):
    return render(request, "questionOK.html")

def question_update(request, member_pk):
    return render(request, "question_update.html")

def question_detail(request, member_pk):
    return render(request, "question_detail.html")

def question_answer(request, member_pk):
    return render(request, "question_answer.html")



from django.shortcuts import render
from service.models import Service

def question_main(request):
    context = {
        'range' : range(5),
    }
    return render(request, "question_main.html", context)

def question_write(request):
    if request.method == "GET":
        return render(request, 'question_write.html')
    elif request.method == "POST":
        title = request.POST['title']
        contents = request.POST['content']
        file = request.POST.get('uploadedFile', None)
        email = request.POST['email']
        p_num = request.POST.get('p_num', None)
    
        PN = Service(
            title = title,
            content = contents,
            file = file,
            phone = p_num,
            email = email
        )
        PN.save()
        # PN = Document.objects.all().order_by("-pk")
        return render(request, 'question_write.html')

def questionOK(request):
    return render(request, "questionOK.html")

def question_update(request):
    return render(request, "question_update.html")

def question_detail(request):
    return render(request, "question_detail.html")

def question_answer(request):
    return render(request, "question_answer.html")



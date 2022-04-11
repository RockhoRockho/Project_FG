from telnetlib import SE
from django.shortcuts import render
from service.models import Service
from member.models import Member
from django.http import Http404

def question_main(request):

    all_service = Service.objects.all().order_by('-id')
    all_count = Service.objects.all().count()

    context = {
        'service' : all_service,
        'count' : all_count,
    }
    
    return render(request, "question_main.html", context)

def question_write(request):
    if request.method == "GET":
        return render(request, 'question_write.html')
    elif request.method == "POST":
        
        member = Member.objects.get(member_id = request.session.get('user'))

        title = request.POST['title']
        contents = request.POST['content']
        file = request.FILES['uploadedFile']
        email = request.POST['email']
        p_num = request.POST.get('p_num', None)
    
        PN = Service(
            member = member,
            title = title,
            content = contents,
            file = file.name,
            phone = p_num,
            email = email
        )
        PN.save()
        # PN = Document.objects.all().order_by("-pk")
        return render(request, 'questionOKk.html', {'id':PN.id})

def questionOK(request):
    return render(request, "questionOK.html")

def question_update(request):
    return render(request, "question_update.html")

def question_detail(request, id):
    try:
        ser = Service.objects.get(id=id)

        ser.save()

    except ser.DoesNotExist:
        raise Http404('게시글을 찾을 수 없습니다')

    return render(request, 'question_detail.html', {'service': ser})

def question_delete(request):
    if request.method == "POST":
        id = request.POST['id']
        print('------------------------------------------')
        ser = Service.objects.get(id=id)
        ser.delete()

        return render(request, 'deleteOK.html')


def question_answer(request):
    return render(request, "question_answer.html")
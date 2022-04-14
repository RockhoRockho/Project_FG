from telnetlib import SE
from django.shortcuts import redirect, render
from service.models import Service
from member.models import Member
from django.http import Http404
from django.core.paginator import Paginator

def question_main(request):

    if request.session.get('user') :
        all_service = Service.objects.all().order_by('-id')
        all_count = Service.objects.all().count()

        write_pages = int(request.session.get('write_pages', 3))
        per_page = int(request.session.get('per_page', 5))
        page = int(request.GET.get('page', 1))

        paginator = Paginator(all_service, per_page)
        page_obj = paginator.get_page(page)
        
        start_page = ((int)((page_obj.number - 1) / write_pages) * write_pages) + 1
        end_page = start_page + write_pages - 1

        if end_page >= paginator.num_pages:
            end_page = paginator.num_pages

        context = {
            'boards' : page_obj,
            'service' : all_service,
            'count' : all_count,
            'write_pages': write_pages,
            'start_page': start_page,
            'end_page': end_page,
            'page_range': range(start_page, end_page + 1),
        }
        
        return render(request, "question_main.html", context)

    else:
        return redirect('/member/needlogin/')

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

def question_update(request, id):
    if request.method == "GET":
        try:
            ser = Service.objects.get(id=id)
        except Service.DoesNotExist:
            raise Http404('게시글을 찾을 수 없습니다.')
        return render(request, "question_update.html", {'service':ser})
    
    elif request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        file = request.FILES['uploadedFile']
        email = request.POST['email']
        p_num = request.POST['phone_num']

        ser = Service.objects.get(id=id)
        ser.title = title
        ser.content = content
        ser.file = file
        ser.email = email
        ser.phone = p_num
        ser.save()

        return render(request, 'updateOK.html', {'id':ser.id})

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
        ser = Service.objects.get(id=id)
        ser.delete()

        return render(request, 'deleteOK.html')


def question_answer(request):
    return render(request, "question_answer.html")
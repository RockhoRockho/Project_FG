from django.shortcuts import render
from member.models import Member

def member_login(request):
    context={

    }
    return render(request, 'member_login.html', context)
    
def member_join(request):
    if request.method =='GET':
        return render(request, 'member_join.html')
    elif request.method== 'POST':
        username = request.POST['username']
        pw = request.POST['pw']
        name = request.POST['name']
        birth = request.POST['pw']
        email = request.POST['email']
        phoneNum = request.POST['phoneNum']
    
        memberT = Member(username = username, pw= pw, name = name, birth = birth, email = email, phoneNum = phoneNum)
        memberT.save()
        return render(request, 'member.html', {'pk': memberT.pk})

def member_terms(request):
    return render(request, "member_terms.html")

def member_info(request):
    return render(request, "member_info.html")

def member_check(request):
    return render(request, "member_check.html")

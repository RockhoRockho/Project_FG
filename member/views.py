from django.http import HttpResponse
from django.shortcuts import render, redirect
from member.models import Member



def member_login(request):
    context = {
        'user': None,
    }
    
    if request.method == "GET":
        print(request.session.get('user'))
        if request.session.get('user'):
            context = {
                'user': request.session.get('user'),
            }
        
        return render(request, 'member_login.html', context)
    elif request.method == "POST":
        login_username = request.POST.get('username', None)
        login_password = request.POST.get('password', None)

        if not (login_username and login_password):
            context = {
                'user': request.session.get('user'),
                'error': "아이디와 비밀번호를 모두 입력하세요."
            }
    
        else:
            myuser = Member.objects.get(username = login_username)
            
            if (login_password == myuser.pw):
                request.session['user'] = myuser.member_id
                print(request.session['user'])
                return redirect('/')
            else:
                context = {
                    'user': request.session.get('user'),
                    'error': '비밀번호가 틀립니다.'
                }
        
        return render(request, 'member_login.html', context)

def home(request):
    user_id = request.session.get('user')
    if user_id:
        myuser_info = Member.objects.get(pk=user_id)
        return HttpResponse(myuser_info.username)

    return HttpResponse('로그인을 해주세요.')

def member_logout(request):
    if request.session.get('user'):
        del(request.session['user'])
    context = {
          'user': request.session.get('user'),
    }

    return render(request, 'member_logout.html', context)

def member_join(request):
    if request.method =='GET':
        context = {
            'user': request.session.get('user'),
        }
        return render(request, 'member_join.html', context)

    elif request.method == 'POST':
        username = request.POST['username']
        pw = request.POST['pw']
        name = request.POST['name']
        gender = 'w'
        birth = request.POST['birth']
        email = request.POST['email']
        phoneNum = request.POST['phoneNum']
    
        memberT = Member(
            username = username,
            pw= pw,
            name = name,
            gender = gender,
            birth = birth, 
            email = email, 
            phoneNum = phoneNum)

        memberT.save()
        
        return render(request, 'main.html')

def member_terms(request):
    context = {
        'user': request.session.get('user'),
    }

    return render(request, "member_terms.html", context)

def member_info(request):
    member = Member.objects.get(member_id = request.session.get('user'))

    if request.method == "GET":
        context = {
            'user': member
        }
        print(member.birth)
        return render(request, "member_info.html", context)
    elif  request.method == "POST":

        memberT = Member.objects.get(member_id = request.session.get('user'))
        name = request.POST['name']
        
        birth = request.POST['birth']
        email = request.POST['email']
        phoneNum = request.POST['phoneNum']

        memberT.name = name
        memberT.birth = birth
        memberT.email = email
        memberT.phoneNum = phoneNum
        memberT.save()
        return render(request, "member_updateOK.html")

def member_check(request):
    return render(request, "member_check.html")

def member_needlogin(request):
    return render(request, "member_needlogin.html")

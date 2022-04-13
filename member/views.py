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

def member_findusername(request):
    name = request.POST['name']
    phoneNum = request.POST.get('phoneNum', None)
    email = request.POST.get('email', None)
    ulst = []
    memberT = Member.objects.all()
    if (name and phoneNum):
        for i in memberT:
            if (i.name == name and i.phoneNum == int(phoneNum)):
                ulst.append(i.username)
            

    elif (name and email):
        for i in memberT:
            if (i.name == name and i.email == email):
                ulst.append(i.username)
    
    if len(ulst) == 0:
        ulst.append('찾은 결과가 없습니다')
        
    context = {
        'ulst' : ulst
    }

    return render(request, 'member_found.html', context)

def member_findpw(request):
    username = request.POST['username']
    name = request.POST['name']
    phoneNum = request.POST.get('phoneNum', None)
    email = request.POST.get('email', None)
    pwlst = []
    memberT = Member.objects.all()
    if (username and name and phoneNum):
        for i in memberT:
            if (i.name == name and i.phoneNum == int(phoneNum) and i.username == username):
                pwlst.append(i.pw)


    elif (username and name and email):
        for i in memberT:
            if (i.name == name and i.email == email and i.username == username):
                pwlst.append(i.pw)


    if len(pwlst) == 0:
        pwlst.append('찾은 결과가 없습니다')
        
    context = {
        'pwlst' : pwlst
    }

    return render(request, 'member_found.html', context)

def member_found(request):
    return render(request, "member_found.html")


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
        
        check = Member.objects.all()
        for i in check:
            if i.username == username:
                context = {
                    'error': '이미 존재하는 아이디입니다.'
                }
                print(i)
                return render(request, 'member_join.html', context)
            else:
                memberT = Member(
                    username = username,
                    pw= pw,
                    name = name,
                    gender = gender,
                    birth = birth, 
                    email = email, 
                    phoneNum = phoneNum)

                memberT.save()
            
                return render(request, 'member_login.html')

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

from django.http import HttpResponse
from django.shortcuts import render, redirect
from member.models import Member

def member_login(request):
    response_data = {}

    if request.method == "GET":
        return render(request, 'member_login.html')
    elif request.method == "POST":
        login_username = request.POST.get('username', None)
        login_password = request.POST.get('password', None)

        print ("안녕!!===============================================================")
        if not (login_username and login_password):
            response_data['error']="아이디와 비밀번호를 모두 입력하세요."
    
        else:
            myuser = Member.objects.get(username = login_username)

            print ("===============================================================")
            print (myuser.pw)
            print (login_password)
            print ("===============================================================")
            
            if (login_password == myuser.pw):
                request.session['user'] = myuser.member_id
                print ("성공===============================================================")
                print(request.session)
                return redirect('/')
            else:
                print ("실패===============================================================")
                response_data['error'] = '비밀번호가 틀립니다.'

        context = {
            'user': request.session.get('user'),
        }
        
        return render(request, 'member_login.html', (response_data, context))

def home(request):
    user_id = request.session.get('user')
    if user_id:
        myuser_info = Member.objects.get(pk=user_id)
        return HttpResponse(myuser_info.username)

    return HttpResponse('로그인을 해주세요.')

def member_logout(request):
    print(request.session.get('user'))
    print(request.session)
    if request.session.get('user'):
        del(request.session['user'])
        return render(request, 'main.html')

def member_join(request):
    if request.method =='GET':
        return render(request, 'member_join.html')
    elif request.method == 'POST':
        # print(request.POST['username'])
        username = request.POST['username']
        pw = request.POST['pw']
        name = request.POST['name']
        gender = 'w'
        birth = request.POST['birth']
        email = request.POST['email']
        phoneNum = request.POST['phoneNum']
        
        #username = request.POST.get('username')
        #pw = request.POST.get('pw')
        #name = request.POST.get('name')
        #gender = 'w'
        #birth = request.POST.get('birth')
        #email = request.POST.get('email')
        #phoneNum = request.POST.get('phoneNum')
        
        memberT = Member(
            username = username,
            pw= pw,
            name = name,
            gender = gender,
            birth = birth, 
            email = email, 
            phoneNum = phoneNum)

        memberT.save()
        
        return render(request, 'member/login.html')

def member_terms(request):
    return render(request, "member_terms.html")

def member_info(request):
    return render(request, "member_info.html")

def member_check(request):
    return render(request, "member_check.html")

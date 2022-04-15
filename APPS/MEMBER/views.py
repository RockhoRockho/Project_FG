from django.http import HttpResponse
from django.shortcuts import render, redirect
from APPS.MEMBER.models import Member

def member_login(request):
    context = {
        'member': request.session.get('user'),
        'error': '',
    }
    if request.method == 'GET':
        return render(request, 'member_login.html', context)
    elif request.method == 'POST':
        memberID = request.POST.get('username', None)
        memberPW = request.POST.get('password', None)

        if not memberID and  not memberPW:
            context['error'] = "아이디와 비밀번호를 모두 입력하세요."
        else:
            try:
                member = Member.objects.get(username=memberID)
            except Member.DoesNotExist:
                member = None

            if not member:
                context['error'] = '없는 계정입니다.'
            elif not memberPW == member.pw:
                context['error'] = '비밀번호가 틀립니다.'
            else:
                context['member'] = request.session.get('user')
                request.session['user'] = member.member_id
                return redirect('/')
        return render(request, 'member_login.html', context)

def member_terms(request):
    context = {
        'member': request.session.get('user'),
        'error': '',
    }

    return render(request, 'member_terms.html', context)

def member_terms_detail(request):
    context = {
        'member': request.session.get('user'),
        'error': '',
    }
    return render(request, 'member_terms_detail.html', context)

def member_findusername(request):
    context = {
        'member': request.session.get('user'),
        'error': '',
    }

    name = request.POST['name']
    phoneNum = request.POST.get('phoneNum', None)
    email = request.POST.get('email', None)
    ulst = []

    try:
        member = Member.objects.get(name=name)
    except Member.DoesNotExist:
        member = None

    if name and phoneNum:
        if member.name == name and member.phoneNum == int(phoneNum):
            ulst.append(member.username)
        else:
            ulst.append('찾은 결과가 없습니다')
    if name and email:
        if member.name == name and member.email == email:
            ulst.append(member.username)
        else:
            ulst.append('찾은 결과가 없습니다')

    context['ulst'] = ulst;

    return render(request, 'member_found.html', context)

def member_findpw(request):
    context = {
        'member': request.session.get('user'),
        'error': '',
    }

    username = request.POST['username']
    name = request.POST['name']
    phoneNum = request.POST.get('phoneNum', None)
    email = request.POST.get('email', None)
    pwlst = []
    
    try:
        member = Member.objects.get(username=username)
    except Member.DoesNotExist:
        member = None

    if username and name and phoneNum:
        if member.username == username and member.name == name and member.phoneNum == int(phoneNum):
            pwlst.append(member.pw)
        else:
            pwlst.append('찾은 결과가 없습니다')
    if username and name and email:
        if member.username == username and member.name == name and member.email == email:
            pwlst.append(member.pw)
        else:
            pwlst.append('찾은 결과가 없습니다')
        
    context['pwlst'] = pwlst;

    return render(request, 'member_found.html', context)

def member_found(request):
    context = {
        'member': request.session.get('user'),
        'error': '',
    }
    return render(request, "member_found.html", context)

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
        'member': request.session.get('user'),
        'error': '',
    }

    return render(request, 'member_logout.html', context)

def member_join(request):
    context = {
        'user': request.session.get('user'),
    }

    if request.method =='GET':
        return render(request, 'member_join.html', context)
    elif request.method == 'POST':
        username = request.POST['username']
        pw = request.POST['pw']
        name = request.POST['name']
        gender = 'm/w'
        birth = request.POST['birth']
        email = request.POST['email']
        phoneNum = request.POST['phoneNum']

        try:
            member = Member.objects.get(username=username)
        except Member.DoesNotExist:
            member = None

        if member:
            context['error'] = '이미 존재하는 아이디입니다.';
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
        pw = request.POST['pw']
        gender = request.POST['gender']
        

        memberT.name = name
        memberT.pw = pw
        memberT.gender = gender
        memberT.birth = birth
        memberT.email = email
        memberT.phoneNum = phoneNum
        memberT.save()
        return render(request, "member_updateOK.html")

def member_needlogin(request):
    return render(request, "member_needlogin.html")

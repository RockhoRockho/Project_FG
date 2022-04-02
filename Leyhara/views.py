from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request, 'main.html');

def register(request):
    return render(request, 'register.html');

def register_personal(request):
    return render(request, 'register_personal.html');

def login_check(request):
    return render(request, 'login_check.html');
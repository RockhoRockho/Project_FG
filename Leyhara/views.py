from django.shortcuts import render

# Create your views here.
def register(request):
    return render(request, 'register.html');

def register_personal(request):
    return render(request, 'register_personal.html');
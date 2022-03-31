from multiprocessing import context
from django.shortcuts import render

# Create your views here.
def login(request):
    context={

    }
    return render(request, 'login1.html', context)
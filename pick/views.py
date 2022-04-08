from django.shortcuts import render

def pick(request):
    context = {
        'range' : range(3),
    }

    return render(request, 'pick.html', context) 
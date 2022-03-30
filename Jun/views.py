from django.shortcuts import render

def search_best(request):
    context = {
        'number' : 25,
    }
    return render(request, 'search_best.html', context)

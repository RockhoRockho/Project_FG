from django.shortcuts import render

def search_best(request):
    context = {
        'range' : range(25),
    }
    return render(request, 'search_best.html', context)

def search_category(request):
    context = {
        'range' : range(25),
    }
    return render(request, 'search_category.html', context)

def cart(request):
    context = {
        
    }
    return render(request, 'cart.html', context)

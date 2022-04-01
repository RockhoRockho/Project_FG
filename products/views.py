from django.shortcuts import render

def search(request):

    return render(request, 'search.html')

def order_by_rate(request):
    context = {
        'range' : range(25),
    }
    return render(request, 'order_by_rate.html', context)

def order_by_view(request):
    context = {
        'range' : range(25),
    }
    return render(request, 'order_by_view.html', context)

def search_error(request):

    return render(request, 'search_error.html')

def review(request):
    return render(request, 'review.html')

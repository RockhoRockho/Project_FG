from django.shortcuts import render
from django.core.paginator import Paginator

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

def reviewed(request):


    # write_pages = int(request.session.get('write_pages', 10))
    # per_page = int(request.session.get('per_page', 5)) 
    # page = int(request.GET.get('page', 1))

    # paginator = Paginator(all_boards)

    context = {
        'range' : range(5),
    }
    return render(request, 'reviewed.html', context)

def present_view(request):
    return render(request, 'present_view.html')

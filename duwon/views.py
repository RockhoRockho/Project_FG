from django.http import Http404
from django.shortcuts import render

def product_detail(request):
    context = {
        'range1' : range(1, 26),
        'range2' : range(5),
        'range3' : range(3),
    }
    #try:
    #    ProductT = Product.objects.get(pk=pk) 
    #    ProductT.save() 
    #except Product.DoesNotExist:
    #    raise Http404('제품을 찾을수 없습니다')

    return render(request, 'detail.html', context) 


def order(request):
    context = {
        'range' : range(3),
    }

    return render(request, 'order.html', context) 

def order_detail(request):
    context = {
        'range' : range(3),
    }
    #try:
    #    ProductT = Product.objects.get(pk=pk) 
    #    ProductT.save() 
    #except Product.DoesNotExist:
    #    raise Http404('제품을 찾을수 없습니다')

    return render(request, 'order_detail.html', context) 
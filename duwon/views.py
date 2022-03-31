from django.http import Http404
from django.shortcuts import render

def product_detail(request):
    context = {
        'range' : range(1, 26),
    }
    #try:
    #    ProductT = Product.objects.get(pk=pk) 
    #    ProductT.save() 
    #except Product.DoesNotExist:
    #    raise Http404('제품을 찾을수 없습니다')

    return render(request, 'detail.html', context) 
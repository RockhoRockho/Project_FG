from django.shortcuts import render

def product_search(request, product_name):

    return render(request, 'product_search.html')

def product_rate(request, product_name):
    context = {
        'range' : range(25),
    }
    return render(request, 'product_rate.html', context)

def product_view(request, product_name):
    context = {
        'range' : range(25),
    }
    return render(request, 'product_view.html', context)

def product_error(request, product_name):

    return render(request, 'product_error.html')

def product_best(request):
    context = {
        'range' : range(25),
        'product_id' : '',
        'product_name' : '',
        'product_price' : '',
        'product_rating' : '', # review 평점 평균으로 계산
        'product_delivery': '',
        'seller_name': '',
    }
    return render(request, 'product_best.html', context)

def product_category(request, category):
    context = {
        'range' : range(25),
        'product_id' : '',
        'category' : '',
        'product_name' : '',
        'product_price' : '',
        'product_rating' : '', # review 평점 평균으로 계산
        'product_delivery': '',
        'seller_name': '',
        'product_category': '',
    }
    return render(request, 'product_category.html', context)

def product_detail(request, product_id):
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

    return render(request, 'product_detail.html', context) 
from django.shortcuts import render

def search_best(request):
    context = {
        'range' : range(25),
        'product_id' : '',
        'product_name' : '',
        'product_price' : '',
        'product_rating' : '', # review 평점 평균으로 계산
        'product_delivery': '',
        'seller_name': '',
    }
    return render(request, 'search_best.html', context)

def search_category(request):
    context = {
        'range' : range(25),
        'product_id' : '',
        'product_name' : '',
        'product_price' : '',
        'product_rating' : '', # review 평점 평균으로 계산
        'product_delivery': '',
        'seller_name': '',
        'product_category': '',
    }
    return render(request, 'search_category.html', context)

def cart(request):
    context = {
        'items' : range(3),
        'zero' : range(0)
    }
    return render(request, 'cart.html', context)

def purchase(request):
    context = {
        'items' : range(0),
        'zero' : range(0)
    }
    return render(request, 'purchase.html', context)

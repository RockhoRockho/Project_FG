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
        'items' : range(3), # order_items_id 수
        'recommend': range(4),
        'zero' : range(0),
        'range' : range(25),
        'product_id' : '',
        'product_name' : '',
        'product_price' : '',
        'product_count': '',
        'order_items_price': '', # product_count * product_price
        'product_rating' : '', # review 평점 평균으로 계산
        'product_delivery': '',
        'seller_name': '',
    }
    return render(request, 'cart.html', context)

def purchase(request):
    context = {
        'items' : range(10), # order_items_id 수
        'order_id': '',
        'order_date': '',
        'member_id': '',
        'member_name': '',
        'receiver_name': '',
        'delivery_address': '',
        'product_id' : '',
        'product_name' : '',
        'product_img' : '',
        'seller_name': '',
        'product_price' : '',
        'cart_items_quantity': '',
    }
    return render(request, 'purchase.html', context)

def purchase_success(request):
    context = {
        'items' : range(2), # order_items_id 수
        'recommend': range(4),
        'order_id': '',
        'order_date': '',
        'member_id': '',
        'member_name': '',
        'receiver_name': '',
        'delivery_address': '',
        'product_id' : '',
        'product_name' : '',
        'product_img' : '',
        'seller_name': '',
        'product_price' : '',
        'cart_items_quantity': '',
    }
    return render(request, 'purchase_success.html', context)

def present(request):
    context = {
        'items' : range(2), # order_items_id 수
        'order_id': '',
        'order_date': '',
        'member_id': '',
        'member_name': '',
        'receiver_name': '',
        'delivery_address': '',
        'product_id' : '',
        'product_name' : '',
        'product_img' : '',
        'seller_name': '',
        'product_price' : '',
        'cart_items_quantity': '',
    }
    return render(request, 'present.html', context)

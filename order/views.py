from django.shortcuts import render

def order_list(request):
    context = {
        'range' : range(3),
    }

    return render(request, 'order_list.html', context) 

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

def order_cart(request):
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
    return render(request, 'order_cart.html', context)

def order_purchase(request):
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
    return render(request, 'order_purchase.html', context)

def order_success(request):
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
    return render(request, 'order_success.html', context)

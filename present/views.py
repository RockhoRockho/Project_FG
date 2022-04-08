from django.shortcuts import render

def present_list(request):
    context = {
        'items' : range(4),
        'recommend' : range(4),
    }
    return render(request, 'present_list.html', context)

def present_send(request):
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
    return render(request, 'present_send.html', context)
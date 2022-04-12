from django.shortcuts import render, redirect
from product.models import Product
from .models import Cart

def order_list(request):
    if request.session.get('user') :
        context = {
            'range' : range(3),
        }

        return render(request, 'order_list.html', context) 
    else:
        return redirect('/member/login/')

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
    items = []
    prodItm = []    
    sum = 0
    all_cart = list(Cart.objects.all().order_by('id'))
    for i in all_cart:
        if i.member_id == request.session.get('user'):
            prod = Product.objects.get(pk=i.product_id)
            sum += int(prod.price) * i.quantity
            prodItm.append(prod)
            items.append(i)
    context = {
        'items' : items,
        'prods' : prodItm,
        'recommend': range(4),
        'zero' : range(0),
        'sum' : format(sum, ',')
    }

    return render(request, 'order_cart.html', context)

def cart_update(request, product_id):
    stock = request.POST['stock']
    cart = Cart.objects.get(product_id=product_id)
    cart.quantity = stock
    cart.save()

    return render(request, 'cart_update.html')

def cart_delete(request, product_id):
    cart = Cart.objects.get(product_id=product_id)
    cart.delete()

    return render(request, 'cart_delete.html')

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
from django.shortcuts import render, redirect
from product.models import Product
from .models import Cart, Order_items

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
    if request.method == "GET":
        product = Cart.objects.all()
    
        cartt = []
        pprod = []
        sum = 0
        all_product = list(Cart.objects.all())
        for i in all_product:
            if i.member_id == request.session.get('user'):
                prod = Product.objects.get(pk=i.product_id)
                pprod.append(prod)
                cartt.append(i)
                sum += int(prod.price) * i.quantity
                print(pprod)

        context = {
            'cartt' : cartt,
            'prods' : pprod,
            'sum' : format(sum, ','),
        }

        return render(request, 'order_purchase.html', context)

    elif request.method == "POST":
        member = Member.objects.get(member_id=request.session.get('user'))
        product = Product.objects.get(id=Order_items.product_id)
        
        print(product)

        delivery_address = request.POST['delivery_address']
        detail_address = request.POST['detail_address']
        receiver_phone = request.POST['phone_firstNum']+'-'+request.POST['phone_secondNum']+'-'+request.POST['phone_threeNum']
        select_list = request.POST['select_list']
        receiver_name = request.POST['receiver_name']

        ord = Order(
            member = member,
            delivery_address = delivery_address,
            detail_address = detail_address,
            receiver_phone = receiver_phone,
            select_list = select_list,
            receiver_name = receiver_name,
        )
        ord.save()

        all_order = Order.objects.all().order_by('-id')

        context = {
            'ood' : all_order,
            'product' : product,
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
from django.shortcuts import render, redirect
from APPS.ORDER.models import Cart, Order_items, TempOrder, Order
from APPS.PRODUCT.models import Product
from datetime import datetime
import requests
import json
import random
from django.core.paginator import Paginator


def order_list(request):
    all_Order_items = list(Order_items.objects.all().order_by('id'))
    all_count = Order_items.objects.filter(member_id=request.session.get('user')).count()

    write_pages = int(request.session.get('write_pages', 3))
    per_page = int(request.session.get('per_page', 2))
    page = int(request.GET.get('page', 1))

    paginator = Paginator(all_Order_items, per_page)
    page_obj = paginator.get_page(page)

    start_page = ((int)((page_obj.number - 1) / write_pages) * write_pages) + 1
    end_page = start_page + write_pages - 1

    if end_page >= paginator.num_pages:
        end_page = paginator.num_pages

    context = {
        'count' : all_count,
        'boards': page_obj,
        'write_pages': write_pages,
        'start_page': start_page,
        'end_page': end_page,
        'page_range': range(start_page, end_page + 1),
    }
    if context['member']:
        orders = Order.objects.filter(member_id=context['member'])
        context['orders'] = orders

        return render(request, 'order_list.html', context)
    else:
        return redirect('/member/needlogin/', context)

def order_cart(request):
    context = {
    }

    if request.session.get('user'):
        items = []
        prodItm = []
        sum = 0
        member_id = request.session['user']

        cart = Cart.objects.filter(member_id=member_id)

        for item in cart:
            if item.member_id == member_id:
                prod = Product.objects.get(product=item.product_id)
                sum += int(prod.price) * item.quantity
                prodItm.append(prod)
                items.append(item)

        random_object = []
        count = Product.objects.count()
        for i in range(4):
            random_object.append(Product.objects.all()[random.randint(0, count - 1)]) 
        
        context['items'] = items
        context['prods'] = prodItm
        context['recommend'] = random_object
        context['blank'] = []
        context['sum'] = format(sum, ',')

        return render(request, 'order_cart.html', context)

    else:
        return redirect('/member/needlogin/')

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

def order_purchase(request, product_id):
    context = {
    }

    if request.method == "GET":
        # ?????? ????????? ????????????
        item = TempOrder.objects.get(product_id=product_id)
        prod = Product.objects.get(pk=product_id)
        sum = int(prod.price) * item.quantity

        context['item'] = item
        context['prod'] = prod
        context['sum'] = format(sum, ',')
        context['product_id'] = product_id

        return render(request, 'order_purchase.html', context)

    elif request.method == "POST":
        # ???????????????
        member_id = context['member']
        # order ??????
        receiver_name = request.POST['receiver_name']
        receiver_phone = request.POST['phone_firstNum']+'-'+request.POST['phone_secondNum']+'-'+request.POST['phone_threeNum']
        delivery_address = request.POST['delivery_address']
        detail_address = request.POST['detail_address']
        select_list = request.POST['select_list']

        ord = Order(
            member_id = member_id,
            receiver_name = receiver_name,
            receiver_phone = receiver_phone,
            delivery_address = delivery_address,
            detail_address = detail_address,
            select_list = select_list,
            number = int(datetime.today().strftime('%Y%m%d%H%M')),
        )
        ord.save()

        # order_items ??????
        price = TempOrder.objects.get(product_id=product_id).price
        quantity = TempOrder.objects.get(product_id=product_id).quantity

        Order_items(member_id=member_id, product_id=product_id, price=price, quantity=quantity).save()


        # ???????????? ???????????? ??? ?????????
        request.session['product'] = product_id

        return render(request, 'before_kakao.html')

def cart_purchase(request):
    context = {
    }

    if request.method == "GET":
        cartt = []
        pprod = []
        sum = 0
        member_id = context['member']

        # ????????????
        all_product = list(Cart.objects.all())
        for item in all_product:
            if item.member_id == member_id:
                prod = Product.objects.get(pk=item.product_id)
                pprod.append(prod)
                cartt.append(item)
                sum += int(prod.price) * item.quantity

                # TempOrder ??????
                TempOrder(product_id=prod.pk, member_id=member_id, price=prod.price, quantity=item.quantity).save()

        context['cartt'] = cartt
        context['prods'] = pprod
        context['sum'] = format(sum, ',')

        return render(request, 'cart_purchase.html', context)

    elif request.method == "POST":

        # ???????????????
        member_id = context['member']

        # order ??????
        delivery_address = request.POST['delivery_address']
        detail_address = request.POST['detail_address']
        receiver_phone = request.POST['phone_firstNum']+'-'+request.POST['phone_secondNum']+'-'+request.POST['phone_threeNum']
        select_list = request.POST['select_list']
        receiver_name = request.POST['receiver_name']

        ord = Order(
            member_id = member_id,
            delivery_address = delivery_address,
            detail_address = detail_address,
            receiver_phone = receiver_phone,
            select_list = select_list,
            receiver_name = receiver_name,
            number = int(datetime.today().strftime('%Y%m%d%H%M')),
        )
        ord.save()
        
        # order_items ??????
        prods = list(TempOrder.objects.all().order_by('id'))

        for prod in prods:
            Order_items(product_id=prod.product_id, member_id=member_id, quantity=prod.quantity, price=prod.price).save() 

        return render(request, 'before_kakao.html')

def order_cancel(request):

    TempOrder.objects.all().delete()

    return render(request, 'cancel.html')

def order_success(request):
    
    # ???????????? order ??? ?????????
    order = Order.objects.last()

    context = {
        'number': order.number,
        'delivery_address': order.delivery_address,
        'detail_address' : order.detail_address
    }
    return render(request, 'order_success.html', context)

def before_kakao(request):
    # ????????? ????????? ?????? POST??? 2??? ?????????
    return render(request, 'before_kakao.html')

def kakaopay(request):
    # ???????????? order ??? ?????????
    order = Order.objects.last()
    member_id = request.session.get('user')

    # ???????????????
    # ????????? ??????
    p_name = []
    p_price = 0
    p_qauntity = 0
    # order ????????????

    # ???????????? ??????
    if request.session.get('product') != None:

        product_id = request.session.get('product')
        tmp = TempOrder.objects.get(product_id=product_id)

        if tmp.member_id == member_id:
            p_price += tmp.price
            p_qauntity += tmp.quantity
            p_name.append(Product.objects.get(product=product_id).name)


    # ???????????? ??????
    elif request.session.get('product') == None:
        # ????????? ??????
        for prod in list(TempOrder.objects.all().order_by('-id')):
            if prod.member_id == request.session.get('user'):
                p_name.append(Product.objects.get(product=prod.product_id).name)
                p_price += prod.price
                p_qauntity += prod.quantity

    if request.method == "POST":    

        url = 'https://kapi.kakao.com/v1/payment/ready'
        headers = {
            "Authorization": "KakaoAK " + "e0e68565dbf3a2564757105698677a37",   
            "Content-type": "application/x-www-form-urlencoded;charset=utf-8",  
        }
        params = {
            "cid": "TC0ONETIME",    # ???????????? ??????
            "partner_order_id": order.number,     # ????????????
            "partner_user_id": member_id,    # ?????? ?????????
            "item_name": p_name,        # ?????? ?????? ??????
            "quantity": p_qauntity,                # ?????? ?????? ??????
            "total_amount": p_price,        # ?????? ?????? ??????
            "tax_free_amount": "0",         # ?????? ?????? ?????????
            "approval_url": "http://127.0.0.1:8000/order/kakaopay/approval/", # ?????? ????????? ????????? URL
            "cancel_url": "http://127.0.0.1:8000",  # ?????? ????????? ????????? URL
            "fail_url": "http://127.0.0.1:8000", # ?????? ????????? ????????? URL
        }

        res = requests.post(url, headers=headers, params=params)
        result = json.loads(res.text)
        request.session['tid'] = result['tid']      # ?????? ????????? ????????? tid??? ????????? ??????
        next_url = result['next_redirect_pc_url']   # ?????? ???????????? ????????? url??? ??????

        return redirect(next_url)

    return render(request, 'kakaopay.html')

def approval(request):

    # order ????????????
    order = Order.objects.last()
    # ?????? ?????????
    member_id = request.session.get('user')

    url = 'https://kapi.kakao.com/v1/payment/approve'
    headers = {
        "Authorization": "KakaoAK " + "e0e68565dbf3a2564757105698677a37",
        "Content-type": "application/x-www-form-urlencoded;charset=utf-8",
    }
    params = {
        "cid": "TC0ONETIME",    # ???????????? ??????
        "tid": request.session['tid'],  # ?????? ????????? ????????? ????????? tid
        "partner_order_id": order.number,     # ????????????
        "partner_user_id": member_id,    # ?????? ?????????
        "pg_token": request.GET.get("pg_token"),     # ?????? ??????????????? ?????? pg??????
    }

    res = requests.post(url, headers=headers, params=params)
    amount = json.loads(res.text)['amount']['total']
    res = res.json()
    context = {
        'res': res,
        'amount': amount,
    }
    
    # ???????????? ?????? ????????? db ??????
    if request.session.get('product') != None:
        del(request.session['product'])
        TempOrder.objects.all().delete()
    
    # ???????????? ?????? ??????????????? db ?????? 
    else:
        Cart.objects.all().delete()
        TempOrder.objects.all().delete()

    return render(request, 'approval.html', context)
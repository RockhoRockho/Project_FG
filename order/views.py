from django.shortcuts import render, redirect
from .models import Cart, Order_items, TempOrder, Order
from product.models import Product
from datetime import datetime
import requests
import json
import random

def order_list(request):
    if request.session.get('user') :
        context = {
            'range' : range(3),
        }

        return render(request, 'order_list.html', context) 
    else:
        return redirect('/member/needlogin/')

def order_detail(request):
    context = {
        'range' : range(3),
    }


    return render(request, 'order_detail.html', context) 

def order_cart(request):
    if request.session.get('user') :
        items = []
        prodItm = []    
        sum = 0
        member_id = request.session['user']

        cart = Cart.objects.filter(member_id=member_id)

        for item in cart:
            prod = Product.objects.get(product=item.product_id)
            sum += int(prod.price) * item.quantity
            prodItm.append(prod)
            items.append(item)

        # def random3():
        #     rand_prod = Product.objects.all().aggregate(id=Product('product'))['product']
        #     while True:
        #         pk = random.randint(1, rand_prod)
        #         product1 = Product.objects.filter(pk=pk).first()    
        #         if product1:
        #             return product1
        random_object = []
        count = Product.objects.count()
        for i in range(4):
            random_object.append(Product.objects.all()[random.randint(0, count - 1)]) 
        
        context = {
            'items' : items,
            'prods' : prodItm,
            'recommend': random_object,
            'blank' : [],
            'sum' : format(sum, ',')
        }

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
    if request.method == "GET":

        # 해당 상품만 가져오기
        item = TempOrder.objects.get(product_id=product_id)
        prod = Product.objects.get(pk=product_id)
        sum = int(prod.price) * item.quantity

        context = {
            'item' : item,
            'prod' : prod,
            'sum' : format(sum, ','),
            'product_id' : product_id,
        }

        return render(request, 'order_purchase.html', context)

    elif request.method == "POST":
        # 유저아이디
        member_id = request.session.get('user')
        # order 저장
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

        # order_items 저장
        price = TempOrder.objects.get(product_id=product_id).price
        quantity = TempOrder.objects.get(product_id=product_id).quantity

        Order_items(member_id=member_id, product_id=product_id, price=price, quantity=quantity).save()


        # 세션으로 바로결제 값 넘기기
        request.session['product'] = product_id

        return render(request, 'before_kakao.html')

def cart_purchase(request):
    if request.method == "GET":
    
        cartt = []
        pprod = []
        sum = 0
        member_id = request.session.get('user')

        # 상품나열
        all_product = list(Cart.objects.all())
        for item in all_product:
            prod = Product.objects.get(pk=item.product_id)
            pprod.append(prod)
            cartt.append(item)
            sum += int(prod.price) * item.quantity

            # TempOrder 저장
            TempOrder(product_id=prod.pk, member_id=member_id, price=prod.price, quantity=item.quantity).save()

        context = {
            'cartt' : cartt,
            'prods' : pprod,
            'sum' : format(sum, ','),
        }

        return render(request, 'cart_purchase.html', context)

    elif request.method == "POST":

        # 유저아이디
        member_id = request.session.get('user')

        # order 저장
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
        
        # order_items 저장
        prods = list(TempOrder.objects.all().order_by('id'))

        for prod in prods:
            Order_items(product_id=prod.product_id, member_id=member_id, quantity=prod.quantity, price=prod.price).save() 

        return render(request, 'before_kakao.html')

def order_cancel(request):

    TempOrder.objects.all().delete()

    return render(request, 'cancel.html')

def order_success(request):
    
    # 가장최근 order 로 불러옴
    order = Order.objects.last()

    context = {
        'number': order.number,
        'delivery_address': order.delivery_address,
        'detail_address' : order.detail_address
    }
    return render(request, 'order_success.html', context)

def before_kakao(request):
    # 경로가 바뀌지 않아 POST가 2번 실행됨
    return render(request, 'before_kakao.html')

def kakaopay(request):
    # 가장최근 order 로 불러옴
    order = Order.objects.last()
    member_id = request.session.get('user')

    # 유저아이디
    # 리스트 저장
    p_name = []
    p_price = 0
    p_qauntity = 0
    # order 불러오기

    # 바로결제 경로
    if request.session.get('product') != None:

        product_id = request.session.get('product')
        tmp = TempOrder.objects.get(product_id=product_id)

        p_price += tmp.price
        p_qauntity += tmp.quantity
        p_name.append(Product.objects.get(product=product_id).name)


    # 장바구니 경로
    elif request.session.get('product') == None:
        # 리스트 담기
        for prod in list(TempOrder.objects.all().order_by('-id')):
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
            "cid": "TC0ONETIME",    # 테스트용 코드
            "partner_order_id": order.number,     # 주문번호
            "partner_user_id": member_id,    # 유저 아이디
            "item_name": p_name,        # 구매 물품 이름
            "quantity": p_qauntity,                # 구매 물품 수량
            "total_amount": p_price,        # 구매 물품 가격
            "tax_free_amount": "0",         # 구매 물품 비과세
            "approval_url": "http://127.0.0.1:8000/order/kakaopay/approval/", # 결제 성공시 넘어갈 URL
            "cancel_url": "http://127.0.0.1:8000",  # 결제 취소시 넘어갈 URL
            "fail_url": "http://127.0.0.1:8000", # 결제 실패시 넘어갈 URL
        }

        res = requests.post(url, headers=headers, params=params)
        result = json.loads(res.text)
        request.session['tid'] = result['tid']      # 결제 승인시 사용할 tid를 세션에 저장
        next_url = result['next_redirect_pc_url']   # 결제 페이지로 넘어갈 url을 저장

        return redirect(next_url)

    return render(request, 'kakaopay.html')

def approval(request):

    # order 불러오기
    order = Order.objects.last()
    # 유저 아이디
    member_id = request.session.get('user')

    url = 'https://kapi.kakao.com/v1/payment/approve'
    headers = {
        "Authorization": "KakaoAK " + "e0e68565dbf3a2564757105698677a37",
        "Content-type": "application/x-www-form-urlencoded;charset=utf-8",
    }
    params = {
        "cid": "TC0ONETIME",    # 테스트용 코드
        "tid": request.session['tid'],  # 결제 요청시 세션에 저장한 tid
        "partner_order_id": order.number,     # 주문번호
        "partner_user_id": member_id,    # 유저 아이디
        "pg_token": request.GET.get("pg_token"),     # 쿼리 스트링으로 받은 pg토큰
    }

    res = requests.post(url, headers=headers, params=params)
    amount = json.loads(res.text)['amount']['total']
    res = res.json()
    context = {
        'res': res,
        'amount': amount,
    }

    
    # 바로결제 경로 진행시 db 삭제
    if request.session.get('product') != None:
        del(request.session['product'])
        TempOrder.objects.all().delete()
    
    # 장바구니 경로 결제진행시 db 삭제 
    else:
        Cart.objects.all().delete()
        TempOrder.objects.all().delete()

    return render(request, 'approval.html', context)
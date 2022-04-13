from django.shortcuts import render, redirect
from product.models import Product
from .models import Cart, Order_items
from member.models import Member
from order.models import Order
import requests
import json

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
        context = {
            'items' : items,
            'prods' : prodItm,
            'recommend': range(4),
            'zero' : range(0),
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



def kakaopay(request):
    if request.method == "POST":
        url = 'https://kapi.kakao.com/v1/payment/ready'
        headers = {
            "Authorization": "KakaoAK " + "e0e68565dbf3a2564757105698677a37",   
            "Content-type": "application/x-www-form-urlencoded;charset=utf-8",  
        }
        params = {
            "cid": "TC0ONETIME",    # 테스트용 코드
            "partner_order_id": "partner_order_id",     # 주문번호
            "partner_user_id": "partner_user_id",    # 유저 아이디
            "item_name": "초코파이",        # 구매 물품 이름
            "quantity": "1",                # 구매 물품 수량
            "total_amount": "2200",        # 구매 물품 가격
            "tax_free_amount": "0",         # 구매 물품 비과세
            "approval_url": "http://127.0.0.1:8000/kakaopay/approval/", # 결제 성공시 넘어갈 URL
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
    url = 'https://kapi.kakao.com/v1/payment/approve'
    headers = {
        "Authorization": "KakaoAK " + "e0e68565dbf3a2564757105698677a37",
        "Content-type": "application/x-www-form-urlencoded;charset=utf-8",
    }
    params = {
        "cid": "TC0ONETIME",    # 테스트용 코드
        "tid": request.session['tid'],  # 결제 요청시 세션에 저장한 tid
        "partner_order_id": "partner_order_id",     # 주문번호
        "partner_user_id": "partner_user_id",    # 유저 아이디
        "pg_token": request.GET.get("pg_token"),     # 쿼리 스트링으로 받은 pg토큰
    }

    res = requests.post(url, headers=headers, params=params)
    amount = json.loads(res.text)['amount']['total']
    res = res.json()
    context = {
        'res': res,
        'amount': amount,
    }
    return render(request, 'approval.html', context)
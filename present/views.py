from django.shortcuts import render
from member.models import Member
from product.models import Product
from .models import Present

def present_list(request):
    pres = []
    pprod = []
    user = request.session['user']
    present = Present.objects.filter(member_id=user)
    for i in present:
        pre = Product.objects.get(pk=i.product_id)
        pprod.append(pre) # 상품정보
        pres.append(i) # 선물정보
    context = {
        'presents' : pres, # 선물
        'products' : pprod, # 상품
        'recommend' : range(4)
    }
    return render(request, 'present_list.html', context)

def present_send(request, product_id):
    product = Product.objects.get(product=product_id)
    present = Present.objects.get(product_id=product_id)
    sum = int(product.price) * present.quantity

    context = {
        'product_id' : product_id,
        'present' : present,
        'product' : product,
        'sum' : format(sum, ','),
    }
    if request.method == 'GET':
        return render(request, 'present_send.html', context)

    elif request.method == 'POST':
        receiver = request.POST['receiver']
        phoneNm = request.POST['phoneNm']
        message = request.POST['msg']

        n_present = Present.objects.get(product_id=product_id)
        n_present.receiver_name = receiver
        n_present.receiver_phone = phoneNm
        n_present.message = message
        n_present.save()

        context['present'] = n_present

        request.session['present'] = n_present.id

        return render(request, 'before_kakao.html', context)

def present_cancel(request, product_id):

    present = Present.objects.get(product_id=product_id)
    present.delete()

    return render(request, 'present_cancel.html')

def present_success(request, present_id):
    
    present = Present.objects.get(id=present_id)
    product = Product.objects.get(product=present.product_id)
    sum = present.quantity * product.price

    context = {
        'present' : present,
        'product' : product,
        'sum' : sum,
    }
    
    return render(request, 'present_success.html', context)
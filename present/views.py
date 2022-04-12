from django.shortcuts import render
from product.models import Product
from .models import Present

def present_list(request):
    context = {
        'items' : range(4),
        'recommend' : range(4),
    }
    return render(request, 'present_list.html', context)

def present_send(request, product_id):
    if request.method == 'GET':

        product = Product.objects.get(product=product_id)
        present = Present.objects.get(product_id=product_id)
        sum = int(product.price) * present.quantity

        context = {
            'product_id' : product_id,
            'present' : present,
            'product' : product,
            'sum' : format(sum, ','),
        }
        return render(request, 'present_send.html', context)

    elif request.method == 'POST':
        receiver = request.POST['receiver']
        phoneNm = request.POST['phoneNm']
        message = request.POST['msg']

        present = Present.objects.get(product_id=product_id)
        present.receiver_name = receiver
        present.receiver_phone = phoneNm
        present.message = message
        present.save()

        context = {
            'product_id' : product_id,
            'present' : present,
            'product' : product,
            'sum' : format(sum, ','),
        }
        return render(request, 'present_send.html', context)

def present_cancel(request, product_id):

    present = Present.objects.get(product_id=product_id)
    present.delete()

    return render(request, 'present_cancel.html')

def present_success(request, product_id):
    
    present = Present.objects.get(product_id=product_id)

    context = {
        'present' : present
    }

    return render(request, 'present_success.html', context)
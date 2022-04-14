import re
from urllib.request import Request
from django.shortcuts import render
from order.models import Order_items
from review.models import Review
from product.models import Product
from django.http import Http404

def review(request):
    
    items = []
    prods = []
    sum = 0
    all_items = Order_items.objects.all().order_by('id')

    for i in all_items:
        if i.member_id == request.session.get('user'):
            prod = Product.objects.get(pk=i.product_id)
            prods.append(prod)
            items.append(i)
            sum += i.price * i.quantity

    all_review = Review.objects.all().order_by('-id')
    all_count = Review.objects.all().count()

    context = {
        'items' : items,
        'prods' : prods,
        'sum' : sum,
        'count' : all_count,
    }
    return render(request, 'review.html', context)

def review_detail(request, id):
    try:
        reviews = Review.objects.get(id=id)
        reviews.save()

    except Review.DoesNotExist:
        raise Http404('게시글을 찾을 수 없습니다')

    return render(request, 'review_detail.html', {'review': reviews})

def review_update(request, id):
    if request.method == "GET":
        try:
            reviews = Review.objects.get(id=id)
        except Review.DoesNotExist:
            raise Http404('게시글을 찾을 수 없습니다')

        return render(request, 'review_update.html', {'review': reviews})
    
    elif request.method == "POST":

        # member = Member.objects.get(member_id = request.session.get('user'))
        # detail = request.POST['detail']
        # rating = 4.5
        # print(Order_items)
        # products = Product.objects.get(product=product_id)
        # order_itemss = '1'
        
        # a = Review(
        #     detail = detail,
        #     rating = rating,
        #     member = member,
        #     product = products,
        #     order_items = order_itemss,
        # )
        # a.save()

        detail = request.POST['detail']
        reviews.detail = detail
        items.save()

        return render(request, 'review_updateOk.html', {"id": reviews.id})

    
def review_delete(request):
    if request.method == "POST":
        id = request.POST['id']
        reviews = Review.objects.get(id=id)
        reviews.delete()
        return render(request, 'review_deleteOK.html')
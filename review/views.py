import re
from urllib.request import Request
from django.shortcuts import render
from order.models import Order_items
from review.models import Review
from product.models import Product
from django.http import Http404
from django.core.paginator import Paginator


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

    write_pages = int(request.session.get('write_pages', 3))
    per_page = int(request.session.get('per_page', 3))
    page = int(request.GET.get('page', 1))

    paginator = Paginator(items, per_page)
    page_obj = paginator.get_page(page)

    start_page = ((int)((page_obj.number - 1) / write_pages) * write_pages) + 1
    end_page = start_page + write_pages - 1

    if end_page >= paginator.num_pages:
        end_page = paginator.num_pages

    context = {
        'items' : items,
        'prods' : prods,
        'sum' : sum,
        'count' : all_count,
        'boards': page_obj,
        'write_pages': write_pages,
        'start_page': start_page,
        'end_page': end_page,
        'page_range': range(start_page, end_page + 1),
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
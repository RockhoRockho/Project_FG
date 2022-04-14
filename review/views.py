from django.shortcuts import render
from order.models import Order_items
from review.models import Review
from product.models import Product
from django.http import Http404
from django.core.paginator import Paginator


def review(request):
    
    items = []
    prods = []

    all_items = Order_items.objects.all().order_by('id')
    all_count = Review.objects.all().count()
    user = request.session.get('user')

    for i in all_items:
        if i.member_id == user:
            prod = Product.objects.get(pk=i.product_id)
            prods.append(prod)

            # 리뷰 데이터 저장하기 기존데이터 있으면 저장x
            if not Review.objects.filter(order_items_id=i.id).exists():
                Review(
                    rating = 0,
                    detail = '',
                    member_id = user,
                    order_items_id = i.id,
                    product_id = i.product_id,
                ).save()
            items.append(Review.objects.get(order_items_id=i.id))

    write_pages = int(request.session.get('write_pages', 3))
    per_page = int(request.session.get('per_page', 3))
    page = int(request.GET.get('page', 1))

    paginator = Paginator(items, per_page)
    page_obj = paginator.get_page(page)

    start_page = ((int)((page_obj.number - 1) / write_pages) * write_pages) + 1
    end_page = start_page + write_pages - 1

    if end_page >= paginator.num_pages:
        end_page = paginator.num_pages

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

def review_update(request, id):
    review = Review.objects.get(id=id)
    product = Product.objects.get(product=review.product_id)

    if request.method == "GET":
        try:
            context = {
                'review' : review,
                'product' : product,
                'id' : id
            }
        except Review.DoesNotExist:
            raise Http404('게시글을 찾을 수 없습니다')

        return render(request, 'review_update.html', context)
    
    elif request.method == "POST":

        # 정보가져오기
        rating = request.POST['rating']
        detail = request.POST['detail']

        # update
        review.detail = detail
        review.rating = rating
        review.save()

        return render(request, 'review_updateOk.html')

    
def review_delete(request, id):
    reviews = Review.objects.get(id=id)
    reviews.delete()
    return render(request, 'review_deleteOK.html')
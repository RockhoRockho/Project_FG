from django.shortcuts import render
from order.models import Order_items
from review.models import Review
from product.models import Product
from django.http import Http404

def review(request):
    
    items = []
    prods = []

    all_items = Order_items.objects.all().order_by('id')
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

    context = {
        'items' : items,
        'prods' : prods,
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

    
def review_delete(request):
    if request.method == "POST":
        id = request.POST['id']
        reviews = Review.objects.get(id=id)
        reviews.delete()
        return render(request, 'review_deleteOK.html')
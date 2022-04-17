from django.shortcuts import render
from APPS.PICK.models import Pick
from APPS.PRODUCT.models import Product
from django.core.paginator import Paginator

def pick(request):
    ppick = []
    pprod = []
    all_pick = list(Pick.objects.all().order_by('id'))
    all_count = Pick.objects.filter(member_id=request.session.get('user')).count()
    for i in all_pick:
        if i.member_id == request.session.get('user'):
            prod = Product.objects.get(pk=i.product_id)
            pprod.append(prod)
            ppick.append(i)

    write_pages = int(request.session.get('write_pages', 3))
    per_page = int(request.session.get('per_page', 2))
    page = int(request.GET.get('page', 1))

    paginator = Paginator(all_pick, per_page)
    page_obj = paginator.get_page(page)

    start_page = ((int)((page_obj.number - 1) / write_pages) * write_pages) + 1
    end_page = start_page + write_pages - 1

    if end_page >= paginator.num_pages:
        end_page = paginator.num_pages

    context = {
        'picks' : ppick,
        'prods' : pprod,
        'count' : all_count,
        'boards': page_obj,
        'write_pages': write_pages,
        'start_page': start_page,
        'end_page': end_page,
        'page_range': range(start_page, end_page + 1),
    }
    return render(request, 'pick.html', context)

def pick_update(request, pk):
    if request.method == 'GET':
        pickT = Pick.objects.get(pk=pk)
        context = {
            'pick':pickT,
        }

        return render(request, 'pick_update.html', context)
    elif request.method== 'POST':
        
        reason = request.POST['reason']
        comment = request.POST['comment']

        pickT = Pick.objects.get(pk=pk)
        pickT.reason = reason
        pickT.comment = comment
        pickT.save()
        return render(request, 'pick_updateOk.html', {'pk': pickT.pk})

def pick_delete(request):
    if request.method =='POST':
        id = request.POST['id']
        pickT = Pick.objects.get(id=id)
        pickT.delete()

        return render(request, 'pick_deleteOk.html')
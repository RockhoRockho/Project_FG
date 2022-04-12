from django.shortcuts import render
from pick.models import Pick
from product.models import Product

def pick(request):
    ppick = []
    pprod = []
    all_pick = list(Pick.objects.all().order_by('id'))
    for i in all_pick:
        if i.member_id == request.session.get('user'):
            prod = Product.objects.get(pk=i.product_id)
            pprod.append(prod)
            ppick.append(i)
    context = {
        'picks' : ppick,
        'prods' : pprod,
        
    }
    return render(request, 'pick.html', context)

def pick_update(request, pk):
    if request.method == 'GET':
        pickT = Pick.objects.get(pk=1)
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
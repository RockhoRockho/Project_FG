from django.shortcuts import render
from pick.models import Pick
from member.models import Member

def pick(request):
    x = ['x'] #무시
    all_pick = Pick.objects.all().order_by('id')
    for i in all_pick: #무시
        x.append(i) #무시
    context = {
        'picks' : all_pick,
        'ppp' : x, #무시
    }
    return render(request, 'pick.html', context)

#def pick_update(request):
#    if request.method == 'GET':
#        pk = request.POST['data-bs-whatever']
#        pickT = Pick.objects.get(pk=pk)
#        return render(request, 'pick.html', {'pick':pickT})
#    elif request.method== 'POST':
#        
#        reason = request.POST['reason']
#        comment = request.POST['comment']
#
#        pickT = Pick.objects.get(pk=pk)
#
#        pickT.reason = reason
#        pickT.comment = comment
#        pickT.save()
#        return render(request, 'pickOk.html', {'pk': pickT.pk})
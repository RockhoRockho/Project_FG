from django.shortcuts import render, redirect
from member.models import Recent_search

def main(request):
    if request.method == 'GET':
        return render(request, 'main.html')

    elif request.method == 'POST':
        product_name = request.POST['sch_word']
        page_num = 1
        # search_word = request.POST['sch_word']
        # rcnt_word = Recent_search(search_word=search_word)
        # rcnt_word.save()

        return render(request, 'search.html', {"product_name": product_name, "page_num" : page_num})

        
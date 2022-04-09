from django.shortcuts import render
import os, sys, json
import urllib.request
from member.models import Recent_search

def product_search(request, product_name):
    
    client_id = '1Go9cVzNHoC3yswLKLwt'
    client_secret = "ozy_PNTen4"
    url = "https://openapi.naver.com/v1/search/shop"
    option = "&display=100&sort=sim"    
    query = "?query=" + urllib.parse.quote('{}'.format(product_name))
    url_query = url + query + option
    
    #Open API 검색 요청 개체 설정
    request1 = urllib.request.Request(url_query)
    request1.add_header("X-Naver-Client-Id",client_id)
    request1.add_header("X-Naver-Client-Secret",client_secret)

    #검색 요청 및 처리
    response = urllib.request.urlopen(request1)
    rescode = response.getcode()
    if(rescode == 200):
        res = response.read().decode('utf-8')
        # items = res.get('items')
 
        jrs = json.loads(res)
        items = jrs['items']
        for item in items:
            item['title'] = item['title'].replace("<b>"+product_name+"</b>", "\n")
        
        item = items
        context = {
            'items' : items
        }

    return render(request, 'product_search.html', context=context)

        



def product_rate(request):
    context = {
        'range' : range(25),
    }
    return render(request, 'product_rate.html', context)


def product_view(request):
    context = {
        'range' : range(25),
    }
    return render(request, 'product_view.html', context)


def product_error(request):

    return render(request, 'product_error.html')


def product_best(request):
    context = {
        'range' : range(25),
        'product_id' : '',
        'product_name' : '',
        'product_price' : '',
        'product_rating' : '', # review 평점 평균으로 계산
        'product_delivery': '',
        'seller_name': '',
    }
    return render(request, 'product_best.html', context)


def product_category(request, category):
    context = {
        'range' : range(25),
        'product_id' : '',
        'category' : '',
        'product_name' : '',
        'product_price' : '',
        'product_rating' : '', # review 평점 평균으로 계산
        'product_delivery': '',
        'seller_name': '',
        'product_category': '',
    }
    return render(request, 'product_category.html', context)


def product_detail(request, product_id):
    context = {
        'range1' : range(1, 26),
        'range2' : range(5),
        'range3' : range(3),
    }
    #try:
    #    ProductT = Product.objects.get(pk=pk) 
    #    ProductT.save() 
    #except Product.DoesNotExist:
    #    raise Http404('제품을 찾을수 없습니다')

    return render(request, 'product_detail.html', context) 

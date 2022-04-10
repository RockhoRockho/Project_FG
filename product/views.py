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

        items = json.loads(res)

        context = {
            'items' : items['items']
        }

    return render(request, 'product_search.html', context=context)


def product_lprice(request, product_name):
    if request.method == 'GET':
        return render(request, 'product_lprice.html')

    # elif request.method == 'POST':
    #     client_id = '1Go9cVzNHoC3yswLKLwt'
    #     client_secret = "ozy_PNTen4"
    #     cat_type = 'cartegories'
    #     if 입력값 = 성별o:
    #         cat_type = 'category/gender'
    #     elif 입력값 = 나이:
    #         cat_type = 'category/age'
    #     url = f"https://openapi.naver.com/v1/datalab/shopping/{cat_type}";
    #     body = "{\"startDate\":\"2017-08-01\",\"endDate\":\"2017-09-30\",\"timeUnit\":\"month\",\"category\":[{\"name\":\"패션의류\",\"param\":[\"50000000\"]},{\"name\":\"화장품/미용\",\"param\":[\"50000002\"]}],\"device\":\"pc\",\"ages\":[\"20\",\"30\"],\"gender\":\"f\"}";

    #     request = urllib.request.Request(url)
    #     request.add_header("X-Naver-Client-Id",client_id)
    #     request.add_header("X-Naver-Client-Secret",client_secret)
    #     request.add_header("Content-Type","application/json")
    #     response = urllib.request.urlopen(request, data=body.encode("utf-8"))
    #     rescode = response.getcode()
    #     if(rescode==200):
    #         response_body = response.read().decode("utf-8")
    #         items = json.loads(response_body)

    #         context = {
    #             'range' : range(25),
    #             'items' : items['items']
    #             }

    #     return render(request, 'product_gender.html', context=context)


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


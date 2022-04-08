from django.shortcuts import render
import os, sys, json
import urllib.request

def product_search(request, product_name):
    context = {
        'product_num' : [],
        'product_name' : [],
        'product_price' : [],
        'product_category' : [],
        'mall_name' : [],


# product_name(상품명)
# product_price(가격)
# product_delivery(배송비)
# product_rating(평점)
# seller_name(판매자이름)
# product_category(카테고리)
# recent_search_id(최근검색 id)
# recent_search_name(최근검색이름)
# recent_search_date(최근검색일자)
    }
     
    # def searchtitle(title):
    
    #     client_id = '1Go9cVzNHoC3yswLKLwt'
    #     client_secret = "ozy_PNTen4"


    #     url = "https://openapi.naver.com/v1/search/shop"
    #     option = "&display=100&sort=sim"    
    #     query = "?query=" + urllib.parse.quote(title)
    #     url_query = url + query + option

    #     #Open API 검색 요청 개체 설정
    #     request = urllib.request.Request(url_query)
    #     request.add_header("X-Naver-Client-Id",client_id)
    #     request.add_header("X-Naver-Client-Secret",client_secret)

    #     #검색 요청 및 처리
    #     response = urllib.request.urlopen(request)
    #     rescode = response.getcode()
    #     if(rescode == 200):
    #         return response.read().decode('utf-8')
    #     else:
    #         return None

    # def main():
    #     #검색 질의 요청
    #     res = searchtitle(product_name)

    #     #검색 결과를 json개체로 로딩
    #     jres = json.loads(res)

    #     #검색 결과의 items 목록의 각 항목(post)을 출력
    #     for post in jres['items']:
    #         append

            


    return render(request, 'product_search.html', context)

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
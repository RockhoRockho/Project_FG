from django.shortcuts import render
import os, sys, json
import urllib.request

def product_search(request, product_name):

    context = { 
        'product_num' : [],
        'product_name' : [],
        'product_price' : [],
        'product_image' : [],
        'product_category' : [],
        'product_rating' : [],
        'mall_name' : [],
    }
     
     
    def searchtitle(title):
    
        client_id = '1Go9cVzNHoC3yswLKLwt'
        client_secret = "ozy_PNTen4"


        url = "https://openapi.naver.com/v1/search/shop"
        option = "&display=100&sort=sim"    
        query = "?query=" + urllib.parse.quote(title)
        url_query = url + query + option

        #Open API 검색 요청 개체 설정
        request = urllib.request.Request(url_query)
        request.add_header("X-Naver-Client-Id",client_id)
        request.add_header("X-Naver-Client-Secret",client_secret)

        #검색 요청 및 처리
        response = urllib.request.urlopen(request)
        rescode = response.getcode()
        if(rescode == 200):
            return response.read().decode('utf-8')
        else:
            return None

    def main():
        #검색 질의 요청
        res = searchtitle(product_name)

        #검색 결과를 json개체로 로딩
        jres = json.loads(res)

        #검색 결과의 items 목록의 각 항목(post)을 출력
        for item in jres['items']:
            context['product_num'].append(item['productId'])
            context['product_name'].append(item['title'])
            context['product_price'].append(item['lprice'])
            context['product_image'].append(item['image'])
            context['product_rating'].append(4.5)
            context['product_category'].append(item['category1'])
            context['mall_name'].append(item['mallName'])

        print(context['product_num'])

    if __name__ == '__main__':
        main()

    # item_list = zip(context['product_num'], context['product_name'], context['product_price'], context['product_image'], context['product_category'], context['mall_name'])
    # context

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

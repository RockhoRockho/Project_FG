from django.shortcuts import redirect, render
import os, sys, json
import urllib.request

from .models import Product
from order.models import Cart
from pick.models import Pick
from present.models import Present

import requests


def product_search(request, product_name, page_num):

    client_id = '1Go9cVzNHoC3yswLKLwt'
    client_secret = "ozy_PNTen4"
    url = "https://openapi.naver.com/v1/search/shop"
    display = "&display=100"
    start = "&start="
    start_num = str(1 + (100 * (page_num-1)))
    sort = "&sort=sim"  
    query = "?query=" + urllib.parse.quote('{}'.format(product_name))
    url_query = url + query + display + start + start_num + sort
     
    #Open API 검색 요청 개체 설정
    request1 = urllib.request.Request(url_query)
    request1.add_header("X-Naver-Client-Id",client_id)
    request1.add_header("X-Naver-Client-Secret",client_secret)

    #검색 요청 및 처리
    response = urllib.request.urlopen(request1)
    rescode = response.getcode()
    if(rescode == 200):
        res = response.read().decode('utf-8')

        items = json.loads(res)



        for data in items['items']:
            product = int(data['productId'])
            name = data['title']
            price = data['lprice']
            category = data['category1']
            image = data['image']
            seller = data['mallName']
            Product(product = product, name = name, price = price, category = category, image = image, seller=seller).save()


        context = {
            'items' : items['items'],
            'product_name' : product_name,
            'page_num' : page_num,           

        }

        return render(request, 'product_search.html', context)


def product_lprice(request, product_name, page_num):
    client_id = '1Go9cVzNHoC3yswLKLwt'
    client_secret = "ozy_PNTen4"
    url = "https://openapi.naver.com/v1/search/shop"
    display = "&display=100"
    start = "&start="
    start_num = str(1 + (100 * (page_num-1)))
    sort = "&sort=asc"  
    query = "?query=" + urllib.parse.quote('{}'.format(product_name))
    url_query = url + query + display + start + start_num + sort
     
    #Open API 검색 요청 개체 설정
    request1 = urllib.request.Request(url_query)
    request1.add_header("X-Naver-Client-Id",client_id)
    request1.add_header("X-Naver-Client-Secret",client_secret)

    #검색 요청 및 처리
    response = urllib.request.urlopen(request1)
    rescode = response.getcode()
    if(rescode == 200):
        res = response.read().decode('utf-8')

        items = json.loads(res)


        for data in items['items']:
            product = int(data['productId'])
            name = data['title']
            price = data['lprice']
            category = data['category1']
            image = data['image']
            seller = data['mallName']
            Product(product = product, name = name, price = price, category = category, image = image, seller=seller).save()


        context = {
            'items' : items['items'],
            'product_name' : product_name,
            'page_num' : page_num,           

        }

        return render(request, 'product_lprice.html', context)



def product_view(request, product_name, page_num):
    client_id = '1Go9cVzNHoC3yswLKLwt'
    client_secret = "ozy_PNTen4"
    url = "https://openapi.naver.com/v1/search/shop"
    display = "&display=100"
    start = "&start="
    start_num = str(1 + (100 * (page_num-1)))
    sort = "&sort=date"  
    query = "?query=" + urllib.parse.quote('{}'.format(product_name))
    url_query = url + query + display + start + start_num + sort
     
    #Open API 검색 요청 개체 설정
    request1 = urllib.request.Request(url_query)
    request1.add_header("X-Naver-Client-Id",client_id)
    request1.add_header("X-Naver-Client-Secret",client_secret)

    #검색 요청 및 처리
    response = urllib.request.urlopen(request1)
    rescode = response.getcode()
    if(rescode == 200):
        res = response.read().decode('utf-8')

        items = json.loads(res)


        for data in items['items']:
            product = int(data['productId'])
            name = data['title']
            price = data['lprice']
            category = data['category1']
            image = data['image']
            seller = data['mallName']
            Product(product = product, name = name, price = price, category = category, image = image, seller=seller).save()


        context = {
            'items' : items['items'],
            'product_name' : product_name,
            'page_num' : page_num,           
            'range' : range(25),
        }
        return render(request, 'product_view.html', context)


def product_error(request):

    return render(request, 'product_error.html')


def product_best(request):
    cookies = {
        'NNB': '44MSIBMO5JVGA',
        'ASID': 'dc4bb9510000017e22d53b8a00000074',
        'nx_ssl': '2',
        'page_uid': 'hC6RWwprvxZssRuc7UVssssstL8-096228',
        '_ga': 'GA1.2.1060489265.1617657285',
        '_ga_7VKFYR6RV1': 'GS1.1.1648742785.164.0.1648742785.60',
        'autocomplete': 'use',
        'AD_SHP_BID': '3',
        'BMR': 's=1649423266424&r=https%3A%2F%2Fm.blog.naver.com%2FPostView.naver%3FisHttpsRedirect%3Dtrue%26blogId%3Dwlwl16%26logNo%3D221263372417&r2=https%3A%2F%2Fwww.google.com%2F',
        'nid_inf': '2121336860',
        'NID_JKL': '9aBZueUfaiA5WNGYXNxkY1XvrycQCsNpKoelOHCjYGA=',
        'spage_uid': 'hC6RWwprvxZssRuc7UVssssstL8-096228',
        'sus_val': 'k6yXeAbC9AvXjTFimwhJfa64',
    }

    headers = {
        'authority': 'search.shopping.naver.com',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36',
        'sec-ch-ua-platform': '"Windows"',
        'accept': '*/*',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://search.shopping.naver.com/best/home?categoryCategoryId=50000000&categoryDemo=A00&categoryRootCategoryId=50000000&chartDemo=A00&chartRank=1&period=P1D&windowCategoryId=20000200&windowDemo=A00&windowRootCategoryId=20000200',
        'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
        # Requests sorts cookies= alphabetically
        # 'cookie': 'NNB=44MSIBMO5JVGA; ASID=dc4bb9510000017e22d53b8a00000074; nx_ssl=2; page_uid=hC6RWwprvxZssRuc7UVssssstL8-096228; _ga=GA1.2.1060489265.1617657285; _ga_7VKFYR6RV1=GS1.1.1648742785.164.0.1648742785.60; autocomplete=use; AD_SHP_BID=3; BMR=s=1649423266424&r=https%3A%2F%2Fm.blog.naver.com%2FPostView.naver%3FisHttpsRedirect%3Dtrue%26blogId%3Dwlwl16%26logNo%3D221263372417&r2=https%3A%2F%2Fwww.google.com%2F; nid_inf=2121336860; NID_JKL=9aBZueUfaiA5WNGYXNxkY1XvrycQCsNpKoelOHCjYGA=; spage_uid=hC6RWwprvxZssRuc7UVssssstL8-096228; sus_val=k6yXeAbC9AvXjTFimwhJfa64',
    }

    params = {
        'categoryCategoryId': 'ALL',
        'categoryDemo': 'A00',
        'categoryRootCategoryId': 'ALL',
        'period': 'P1D',
    }

    response = requests.get('https://search.shopping.naver.com/best/_next/data/ujg-R5qV9-5eMECzXWS5R/category/click.json', headers=headers, params=params, cookies=cookies)
    # 여기서부터 추가코드-----------------------------
    itemlist = json.loads(response.text)

    items = itemlist['pageProps']['dehydratedState']['queries'][2]['state']['data']['products']
    
    for data in items:
        product = int(data['nvMid'])
        name = data['productTitle']
        price = data['mobileLowPrice']
        category = data['productName']
        image = data['imageUrl']
        seller = data['mallName']
        if seller is None:
            seller = "네이버"
        Product(product = product, name = name, price = price, category = category, image = image, seller=seller).save()


    context = {
        'items' : items
    }
    return render(request, 'product_best.html', context)


def product_category(request, category):
    cookies = {
        'NNB': '44MSIBMO5JVGA',
        'ASID': 'dc4bb9510000017e22d53b8a00000074',
        'nx_ssl': '2',
        'page_uid': 'hC6RWwprvxZssRuc7UVssssstL8-096228',
        '_ga': 'GA1.2.1060489265.1617657285',
        '_ga_7VKFYR6RV1': 'GS1.1.1648742785.164.0.1648742785.60',
        'autocomplete': 'use',
        'AD_SHP_BID': '3',
        'BMR': 's=1649423266424&r=https%3A%2F%2Fm.blog.naver.com%2FPostView.naver%3FisHttpsRedirect%3Dtrue%26blogId%3Dwlwl16%26logNo%3D221263372417&r2=https%3A%2F%2Fwww.google.com%2F',
        'nid_inf': '2121336860',
        'NID_JKL': '9aBZueUfaiA5WNGYXNxkY1XvrycQCsNpKoelOHCjYGA=',
        'spage_uid': 'hC6RWwprvxZssRuc7UVssssstL8-096228',
        'sus_val': 'k6yXeAbC9AvXjTFimwhJfa64',
    }

    headers = {
        'authority': 'search.shopping.naver.com',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36',
        'sec-ch-ua-platform': '"Windows"',
        'accept': '*/*',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://search.shopping.naver.com/best/home?categoryCategoryId=50000000&categoryDemo=A00&categoryRootCategoryId=50000000&chartDemo=A00&chartRank=1&period=P1D&windowCategoryId=20000200&windowDemo=A00&windowRootCategoryId=20000200',
        'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
        # Requests sorts cookies= alphabetically
        # 'cookie': 'NNB=44MSIBMO5JVGA; ASID=dc4bb9510000017e22d53b8a00000074; nx_ssl=2; page_uid=hC6RWwprvxZssRuc7UVssssstL8-096228; _ga=GA1.2.1060489265.1617657285; _ga_7VKFYR6RV1=GS1.1.1648742785.164.0.1648742785.60; autocomplete=use; AD_SHP_BID=3; BMR=s=1649423266424&r=https%3A%2F%2Fm.blog.naver.com%2FPostView.naver%3FisHttpsRedirect%3Dtrue%26blogId%3Dwlwl16%26logNo%3D221263372417&r2=https%3A%2F%2Fwww.google.com%2F; nid_inf=2121336860; NID_JKL=9aBZueUfaiA5WNGYXNxkY1XvrycQCsNpKoelOHCjYGA=; spage_uid=hC6RWwprvxZssRuc7UVssssstL8-096228; sus_val=k6yXeAbC9AvXjTFimwhJfa64',
    }

    params = {
        'categoryCategoryId': '{}'.format(category),
        'categoryDemo': 'A00',
        'categoryRootCategoryId': '{}'.format(category),
        'period': 'P1D',
    }

    response = requests.get('https://search.shopping.naver.com/best/_next/data/ujg-R5qV9-5eMECzXWS5R/category/click.json', headers=headers, params=params, cookies=cookies)
    # 여기서부터 추가코드-----------------------------
    itemlist = json.loads(response.text)

    items = itemlist['pageProps']['dehydratedState']['queries'][2]['state']['data']['products']
    
    for data in items:
        product = int(data['nvMid'])
        name = data['productTitle']
        price = data['mobileLowPrice']
        category = data['productName']
        image = data['imageUrl']
        seller = data['mallName']
        if seller is None:
            seller = "네이버"
        Product(product = product, name = name, price = price, category = category, image = image, seller=seller).save()


    context = {
        'items' : items,
    }
    return render(request, 'product_category.html', context)


def product_detail(request, product_id):
    if request.session.get('user') :
        detail = Product.objects.filter(product=product_id)
        context = {
            'detail' : detail,
            'product_id' : product_id
        }

        return render(request, 'product_detail.html', context) 
    else:
        return redirect('/member/needlogin/')


def before_cart(request, product_id):

    member_id = request.session.get('user')
    
    if Cart.objects.filter(product_id=product_id).exists():
        cart = Cart.objects.get(product_id=product_id)
        cart.quantity += 1
        cart.save()
    else:
        Cart(product_id = product_id, member_id=member_id).save()
        

    return render(request, 'before_cart.html', {'product_id' : product_id})

def before_pick(request, product_id):

    member_id = request.session.get('user')
    if not Pick.objects.filter(product_id=product_id).exists():
        Pick(product_id = product_id, member_id=member_id).save()
        
    context = {
        'product_id': product_id
    }        
    return render(request, 'before_pick.html', context)

def before_pay(request, product_id):

    member_id = request.session.get('user')
    quantity = request.POST['quantity']
    if not Present.objects.filter(product_id=product_id).exists():
        Present(product_id = product_id, member_id=member_id, quantity=quantity).save()
        
    context = {
        'product_id': product_id
    }        
    return render(request, 'before_pay.html', context)

def before_present(request, product_id):

    member_id = request.session.get('user')
    quantity = request.POST['quantity']
    if not Present.objects.filter(product_id=product_id).exists():
        Present(product_id = product_id, member_id=member_id, quantity=quantity).save()
        
    context = {
        'product_id': product_id
    }        
    return render(request, 'before_present.html', context)
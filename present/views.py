from django.shortcuts import render, redirect
from product.models import Product
from .models import Present
import requests
import json

def present_list(request):
    pres = []
    pprod = []
    user = request.session['user']
    present = Present.objects.filter(member_id=user)
    for i in present:
        if i.member_id == user:
            pre = Product.objects.get(pk=i.product_id)
            pprod.append(pre) # 상품정보
            pres.append(i) # 선물정보

    cookies = {
        'TODAY_PAGE_COOKIE_KEY': '12',
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
        'ncpa': '819556|l1t03ye8|09f6a2c9c0dc247499b546c763a04175dc0a76ad|s_8e72e554622b|b97e3774855446005bc1e081f8a7e5b5e8bc3ed1:306782|l1t1rlrs|ddb134b8760437e4e4e3e19aabc538a18db5de79|s_586355770812110737|bb77570d9b015e45bac193bb95fc6ab13b003473:157411|l1t30j20|ec14cbe7076ac39b7ee2b9de43b06a1ecee0549f|s_ece0724cb27099|4ea81502b709ad00696685bc839251e0208851d8:832436|l1taqs14|dfd1cdc31555020c1e67a5ba9d2fda9f1ade0941|s_3145b2e8442c9|3ef301948df8fd680d7133f5cdd0d1c58a3fa169:95694|l1tay708|a2171ce691fa49c8d3534ae475bcabbc045956ea|null|6f4360e64e9da64816c2323eca75080aad137d79',
        'sus_val': 'nNv1vFFvpsjn4pWevbkb+R+H',
        'spage_uid': 'hC6RWwprvxZssRuc7UVssssstL8-096228',
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
        'referer': 'https://search.shopping.naver.com/best/category/click?categoryCategoryId=ALL&categoryChildCategoryId=&categoryDemo=A00&categoryMidCategoryId=&categoryRootCategoryId=ALL&period=P1D',
        'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
        # Requests sorts cookies= alphabetically
        # 'cookie': 'TODAY_PAGE_COOKIE_KEY=12; NNB=44MSIBMO5JVGA; ASID=dc4bb9510000017e22d53b8a00000074; nx_ssl=2; page_uid=hC6RWwprvxZssRuc7UVssssstL8-096228; _ga=GA1.2.1060489265.1617657285; _ga_7VKFYR6RV1=GS1.1.1648742785.164.0.1648742785.60; autocomplete=use; AD_SHP_BID=3; BMR=s=1649423266424&r=https%3A%2F%2Fm.blog.naver.com%2FPostView.naver%3FisHttpsRedirect%3Dtrue%26blogId%3Dwlwl16%26logNo%3D221263372417&r2=https%3A%2F%2Fwww.google.com%2F; nid_inf=2121336860; NID_JKL=9aBZueUfaiA5WNGYXNxkY1XvrycQCsNpKoelOHCjYGA=; ncpa=819556|l1t03ye8|09f6a2c9c0dc247499b546c763a04175dc0a76ad|s_8e72e554622b|b97e3774855446005bc1e081f8a7e5b5e8bc3ed1:306782|l1t1rlrs|ddb134b8760437e4e4e3e19aabc538a18db5de79|s_586355770812110737|bb77570d9b015e45bac193bb95fc6ab13b003473:157411|l1t30j20|ec14cbe7076ac39b7ee2b9de43b06a1ecee0549f|s_ece0724cb27099|4ea81502b709ad00696685bc839251e0208851d8:832436|l1taqs14|dfd1cdc31555020c1e67a5ba9d2fda9f1ade0941|s_3145b2e8442c9|3ef301948df8fd680d7133f5cdd0d1c58a3fa169:95694|l1tay708|a2171ce691fa49c8d3534ae475bcabbc045956ea|null|6f4360e64e9da64816c2323eca75080aad137d79; sus_val=nNv1vFFvpsjn4pWevbkb+R+H; spage_uid=hC6RWwprvxZssRuc7UVssssstL8-096228',
    }

    params = {
        'categoryCategoryId': 'ALL',
        'categoryChildCategoryId': '',
        'categoryDemo': 'A00',
        'categoryMidCategoryId': '',
        'categoryRootCategoryId': 'ALL',
        'period': 'P1D',
    }

    response = requests.get('https://search.shopping.naver.com/best/_next/data/ujg-R5qV9-5eMECzXWS5R/category/purchase.json', headers=headers, params=params, cookies=cookies)
    
    itemlist2 = json.loads(response.text)

    items2 = itemlist2['pageProps']['dehydratedState']['queries'][2]['state']['data']['products']


    for data in items2:
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
        'presents' : pres, # 선물
        'products' : pprod, # 상품
        'recommend' : items2
    }
    return render(request, 'present_list.html', context)

def present_send(request, product_id):
    product = Product.objects.get(product=product_id)
    present = Present.objects.get(product_id=product_id)
    sum = int(product.price) * present.quantity

    context = {
        'product_id' : product_id,
        'present' : present,
        'product' : product,
        'sum' : format(sum, ','),
    }
    if request.method == 'GET':
        return render(request, 'present_send.html', context)

    elif request.method == 'POST':
        receiver = request.POST['receiver']
        phoneNm = request.POST['phoneNm']
        message = request.POST['msg']

        # Present db 저장
        n_present = Present.objects.get(product_id=product_id)
        n_present.receiver_name = receiver
        n_present.receiver_phone = phoneNm
        n_present.message = message
        n_present.save()

        context['present'] = n_present

        request.session['present'] = n_present.id

        return render(request, 'before_kakao_present.html', context)

def present_cancel(request, product_id):

    present = Present.objects.get(product_id=product_id)
    present.delete()

    return render(request, 'present_cancel.html')

def present_success(request):
    
    present = Present.objects.last()
    product = Product.objects.get(product=present.product_id)
    sum = present.quantity * product.price

    context = {
        'present' : present,
        'product' : product,
        'sum' : sum,
    }
    
    return render(request, 'present_success.html', context)

def before_kakao_present(request):
    # 경로가 바뀌지 않아 POST가 2번 실행됨
    return render(request, 'before_kakao_present.html')

def present_kakaopay(request):
    # 가장최근 Present 로 불러옴
    present = Present.objects.last()
    # 유저아이디
    member_id = request.session.get('user')

    # 리스트 저장
    p_name = []
    p_price = 0
    p_qauntity = 0

    # 선물결제 경로
    present_id = request.session.get('present')
    prod = Present.objects.get(id=present_id)

    # 리스트 담기
    if prod.member_id == member_id:
        product_id = prod.product_id
        p_qauntity += prod.quantity
        p_price += int(Product.objects.get(product=product_id).price)
        p_name.append(Product.objects.get(product=product_id).name)

    if request.method == "POST":    

        url = 'https://kapi.kakao.com/v1/payment/ready'
        headers = {
            "Authorization": "KakaoAK " + "e0e68565dbf3a2564757105698677a37",   
            "Content-type": "application/x-www-form-urlencoded;charset=utf-8",  
        }
        params = {
            "cid": "TC0ONETIME",    # 테스트용 코드
            "partner_order_id": present.id,     # 주문번호
            "partner_user_id": member_id,    # 유저 아이디
            "item_name": p_name,        # 구매 물품 이름
            "quantity": p_qauntity,                # 구매 물품 수량
            "total_amount": p_price,        # 구매 물품 가격
            "tax_free_amount": "0",         # 구매 물품 비과세
            "approval_url": "http://127.0.0.1:8000/present/kakaopay/approval/", # 결제 성공시 넘어갈 URL
            "cancel_url": "http://127.0.0.1:8000",  # 결제 취소시 넘어갈 URL
            "fail_url": "http://127.0.0.1:8000", # 결제 실패시 넘어갈 URL
        }

        res = requests.post(url, headers=headers, params=params)
        result = json.loads(res.text)
        request.session['tid'] = result['tid']      # 결제 승인시 사용할 tid를 세션에 저장
        next_url = result['next_redirect_pc_url']   # 결제 페이지로 넘어갈 url을 저장

        return redirect(next_url)

    return render(request, 'present_kakaopay.html')

def present_approval(request):

    # present 불러오기
    present = Present.objects.last()
    # 유저 아이디
    member_id = request.session.get('user')

    url = 'https://kapi.kakao.com/v1/payment/approve'
    headers = {
        "Authorization": "KakaoAK " + "e0e68565dbf3a2564757105698677a37",
        "Content-type": "application/x-www-form-urlencoded;charset=utf-8",
    }
    params = {
        "cid": "TC0ONETIME",    # 테스트용 코드
        "tid": request.session['tid'],  # 결제 요청시 세션에 저장한 tid
        "partner_order_id": present.id,     # 주문번호
        "partner_user_id": member_id,    # 유저 아이디
        "pg_token": request.GET.get("pg_token"),     # 쿼리 스트링으로 받은 pg토큰
    }

    res = requests.post(url, headers=headers, params=params)
    amount = json.loads(res.text)['amount']['total']
    res = res.json()
    context = {
        'res': res,
        'amount': amount,
    }

    # 선물경로 결제 진행시 db 삭제
    if request.session.get('present') != None:
        del(request.session['present'])

    return render(request, 'present_approval.html', context)
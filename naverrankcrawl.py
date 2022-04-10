import requests
# from bs4 import BeautifulSoup
import urllib
import json

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
    'categoryCategoryId': '50000000',
    'categoryDemo': 'A00',
    'categoryRootCategoryId': '50000000',
    'period': 'P1D',
}

response = requests.get('https://search.shopping.naver.com/best/_next/data/ujg-R5qV9-5eMECzXWS5R/category/click.json', headers=headers, params=params, cookies=cookies)
# 여기서부터 추가코드-----------------------------
itemlist = json.loads(response.text)

itemlist = itemlist['pageProps']['dehydratedState']['queries'][2]['state']['data']['products']
print(itemlist)

for i in itemlist:
    rank = i['rank']
    name = i['productName']
    price = i['mobileLowPrice']
    image = i['imageUrl']
    product_id = i['nvMid']
    
    print(rank, name, price, image, product_id)
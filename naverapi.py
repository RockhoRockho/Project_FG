# # 네이버 검색 API예제는 블로그를 비롯 전문자료까지 호출방법이 동일하므로 blog검색만 대표로 예제를 올렸습니다.
# # 네이버 검색 Open API 예제 - 블로그 검색
import os
import sys
import urllib.request
import json
# client_id = '1Go9cVzNHoC3yswLKLwt'
# client_secret = "ozy_PNTen4"
# encText = urllib.parse.quote("밥") # 검색할 단어 입력
# url = "https://openapi.naver.com/v1/search/shop?query=" + encText # json 결과
# # url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
# request = urllib.request.Request(url)
# request.add_header("X-Naver-Client-Id",client_id)
# request.add_header("X-Naver-Client-Secret",client_secret)
# response = urllib.request.urlopen(request)
# rescode = response.getcode()
# if(rescode==200):
#     response_body = response.read()
#     print(response_body.decode('utf-8'))

# else:
#     print("Error Code:" + rescode)

def searchtitle(title):
    
    client_id = '1Go9cVzNHoC3yswLKLwt'
    client_secret = "ozy_PNTen4"
    
    
    url = "https://openapi.naver.com/v1/search/shop"
    option = "&display=3&sort=count"    
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

#검색 결과 항목 정보 출력하기
def showitem(item):
    print("제목:"+item['title'])
    print("이미지:"+item['image'])
    print("카테고리:"+item['category1'])
    print("================")


#프로그램 진입점
def main():
    #검색 질의 요청
    res = searchtitle(input("질의:"))
    if(res == None):
        print("검색 실패")
        exit()
    #검색 결과를 json개체로 로딩
    jres = json.loads(res)
    if(jres == None):
        print("json.loads 실패")
        exit()
 
    #검색 결과의 items 목록의 각 항목(post)을 출력
    for post in jres['items']:
        showitem(post)
 
#진입점 함수를 main으로 지정
if __name__ == '__main__':
    main()

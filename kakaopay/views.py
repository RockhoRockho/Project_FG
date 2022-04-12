from django.shortcuts import render, redirect
import requests
import json

# Create your views here.
def kakaopay(request):
    if request.method == "POST":
        url = 'https://kapi.kakao.com/v1/payment/ready'
        headers = {
            "Authorization": "KakaoAK " + "e0e68565dbf3a2564757105698677a37",   # 변경불가
            "Content-type": "application/x-www-form-urlencoded;charset=utf-8",  # 변경불가
        }
        params = {
            "cid": "TC0ONETIME",    # 테스트용 코드
            "partner_order_id": "partner_order_id",     # 주문번호
            "partner_user_id": "partner_user_id",    # 유저 아이디
            "item_name": "초코파이",        # 구매 물품 이름
            "quantity": "1",                # 구매 물품 수량
            "total_amount": "2200",        # 구매 물품 가격
            "tax_free_amount": "0",         # 구매 물품 비과세
            "approval_url": "http://IP:8000", # 결제 성공시 넘어갈 URL
            "cancel_url": "http://IP:8000",  # 결제 취소시 넘어갈 URL
            "fail_url": "http://IP:8000", # 결제 실패시 넘어갈 URL
        }

        res = requests.post(url, headers=headers, params=params)
        result = json.loads(res.text)
        request.session['tid'] = result['tid']      # 결제 승인시 사용할 tid를 세션에 저장
        next_url = result['next_redirect_pc_url']   # 결제 페이지로 넘어갈 url을 저장
        return redirect(next_url)


    return render(request, 'kakaopay.html')

def approval(request):
    url = 'https://kapi.kakao.com/v1/payment/approve'
    headers = {
        "Authorization": "KakaoAK " + "e0e68565dbf3a2564757105698677a37",
        "Content-type": "application/x-www-form-urlencoded;charset=utf-8",
    }
    params = {
        "cid": "TC0ONETIME",    # 테스트용 코드
        "tid": request.session['tid'],  # 결제 요청시 세션에 저장한 tid
        "partner_order_id": "partner_order_id",     # 주문번호
        "partner_user_id": "partner_user_id",    # 유저 아이디
        "pg_token": request.GET.get("pg_token"),     # 쿼리 스트링으로 받은 pg토큰
    }

    res = requests.post(url, headers=headers, params=params)
    amount = json.loads(res.text)['amount']['total']
    res = res.json()
    context = {
        'res': res,
        'amount': amount,
    }
    return render(request, 'approval.html', context)


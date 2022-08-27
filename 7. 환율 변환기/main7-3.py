# pip install currencyconverter

import requests
from bs4 import BeautifulSoup

def get_exchange_rate (target1, target2) :      # 환율 구하는 함수
    headers = {         # 헤더 추가
        "User-Agent" : "Mozilla/5.0",
        "Content-Type" : "text/html; charset=utf-8"
    }
    
    response = requests.get("https://kr.investing.com/currencies/{}-{}".format(target1, target2), headers=headers)      # requests 라이브러리 이용, 해당 사이트에 접속하여 응답값 받아오기
    content = BeautifulSoup(response.content, "html.parser")        # beautifulsoup 라이브러리 이용, 값을 보기 좋게 하기 위함
    containers = content.find("span", {"data-test":"instrument-price-last"})        # 마지막 환율 정보 검색
    print(containers.text)
    
get_exchange_rate("usd", "krw")


# <span class="text-2xl" data-test="instrument-price-last">1,304.63</span>
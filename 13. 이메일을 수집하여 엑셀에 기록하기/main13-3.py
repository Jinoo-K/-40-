import requests
# https://me2nuk.com/Python-requests-module-example/ requests 모듈 사용법
import re

url = "https://news.v.daum.net/v/202111291442297"

headers = {     # 헤더 정보 입력, 입력하지 않았을 때 응답하지 않는 사이트가 많음
    "User-Agent" : "Mozilla/5.0",
    "Content-Type" : "text/html; charset=utf-8"
}

response = requests.get(url, headers=headers)       # url로 접속

results = re.findall(r"[\w\.-]+@[\w\.-]+", response.text)

results = list(set(results))

print(results)

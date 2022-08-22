import socket    # socket 모듈 불러오기
import requests    # 사이트에 접속하기 위해 request 모듈 불러오기
import re    # IP주소를 찾기 위한 정규식을 사용하기 위해 re 모듈 불러오기

in_addr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    # 내부 IP 확인 후 출력
in_addr.connect(("www.google.com", 443))
print("내부 IP :",in_addr.getsockname()[0])

req = requests.get("http://ipconfig.kr")    # 외부 IP 확인 후 출력
out_addr = re.search(r'IP Address : (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', req.text)[1]
print("외부 IP : ",out_addr)
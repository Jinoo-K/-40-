import requests    # 사이트에 접속하기 위해 request 모듈 불러오기
import re    # IP주소를 찾기 위한 정규식을 사용하기 위해 re 모듈 불러오기

req = requests.get("http://ipconfig.kr")    # http://ipconfig.kr 사이트 접속
out_addr = re.search(r" IP Address : (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} ", req.text)[1]    # 정규식 표현 사용, IP 주소를 가져와서 out_addr에 변수 선언
print(out_addr)    # ip 주소 출력
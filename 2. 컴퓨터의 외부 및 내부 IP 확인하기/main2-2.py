import socket # socket 모듈 불러오기

ipAddress = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # 소켓 연결
ipAddress.connect(("www.google.com", 443)) # www.google.com 포트 443에 연결
print(ipAddress.getsockname()[0]) # 연결 된 소켓 이름 출력, [0]의 이유는 포트번호가 같이 나오기 때문
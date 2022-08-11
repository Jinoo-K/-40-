import socket # socket 모듈 불러오기

ipAddress = socket.gethostbyname(socket.gethostname()) # 연결된 소켓 이름을 가져와서 ipAddress에 바인딩

print(ipAddress) # ipAddress 출력해서 내부 IP 확인
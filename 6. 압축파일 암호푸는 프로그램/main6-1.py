import itertools

passwd_string = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"        # 숫자, 영어 소문자, 대문자 바인딩

for i in range (1,4) :      # 1~3까지 반복
    to_attempt = itertools.product(passwd_string, repeat=i)     # passwd_string의 모든 문자열을 1~3자리로 정렬하여 반환
    for attempt in to_attempt :     # 반환된 문자의 수만큼 반복
        passwd = ''.join(attempt)       # 리스트로 변환된 값을 문자열로 반환
        print(passwd)
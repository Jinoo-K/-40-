import itertools
import zipfile

passwd_string = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"        # 숫자, 영어 소문자, 대문자 바인딩

zFile = zipfile.ZipFile(r"6. 압축파일 암호푸는 프로그램\암호1234.zip")          # 비밀번호가 걸려있는 압축파일 불러오기

for i in range (1,6) :      # 1~5까지 반복
    to_attempt = itertools.product(passwd_string, repeat = i)     # passwd_string의 모든 문자열을 1~5자리로 정렬하여 반환
    for attempt in to_attempt :     # 반환된 문자의 수만큼 반복
        passwd = ''.join(attempt)       # 리스트로 변환된 값을 문자열로 반환
        print(passwd)
        try :       # 비밀번호 입력, 맞으면 try, 틀리면 except
            zFile.extractall(pwd = passwd.encode())     # 비밀번호 입력, 맞으면 15, 16줄 실행, 틀리면 17, 18줄 실행
            print(f"비밀번호는 {passwd} 입니다.")
            break   # 비밀번호 찾고 for문 종료
        except :
            pass
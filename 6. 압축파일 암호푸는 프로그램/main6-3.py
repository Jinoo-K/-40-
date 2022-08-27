import itertools
import zipfile


def un_zip(passwd_string, min_len, max_len, zFile) :
    for i in range (min_len, max_len+1) :
        to_attempt = itertools.product(passwd_string, repeat = i)     # passwd_string의 모든 문자열을 1~5자리로 정렬하여 반환
        for attempt in to_attempt :     # 반환된 문자의 수만큼 반복
            passwd = ''.join(attempt)       # 리스트로 변환된 값을 문자열로 반환
            print(passwd)
            try :       # 비밀번호 입력, 맞으면 try, 틀리면 except
                zFile.extractall(pwd = passwd.encode())     # 비밀번호 입력, 맞으면 13, 14줄 실행, 틀리면 15, 16줄 실행
                print(f"비밀번호는 {passwd} 입니다.")
                return 1        # 결과값 1
            except :
                pass
            
passwd_string = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"        # 숫자, 영어 소문자, 대문자 바인딩

zFile = zipfile.ZipFile(r"6. 압축파일 암호푸는 프로그램\암호1234.zip")          # 비밀번호가 걸려있는 압축파일 불러오기

min_len = 1
max_len = 5

unzip_result = un_zip(passwd_string, min_len, max_len, zFile)

if unzip_result == 1:
    print("암호찾기에 성공하였습니다.")
else :
    print("암호찾기에 실패하였습니다.")
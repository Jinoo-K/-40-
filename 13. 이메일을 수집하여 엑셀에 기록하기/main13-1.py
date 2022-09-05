import re
# https://brownbears.tistory.com/506    re 모듈 사용법

test_string = """
aaa@bbb.com
123@abc.co.kr
test@hello.kr
ok@ok.co.kr
ok@ok.co.kr
ok@ok.co.kr
no.co.kr
no.kr
"""

result = re.findall(r"[\w\.-]+@[\w\.-]+", test_string)      # 문자열에서 이메일 형식을 찾아 리스트형태로 결과 반환

print(result)

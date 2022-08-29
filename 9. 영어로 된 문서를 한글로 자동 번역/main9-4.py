# pip install googletrans==4.0.0-rc1

import googletrans            # googletrans 모듈 불러오기

translator = googletrans.Translator()

read_file_path = r"9. 영어로 된 문서를 한글로 자동 번역\영어파일.txt"
write_file_path = r"9. 영어로 된 문서를 한글로 자동 번역\한글파일.txt"      # 저장할 경로 및 파일 이름 설정

with open(read_file_path, "r") as f :       # 위의 파일을 줄 별로 읽어서 readLines에 리스트 형태로 바인딩
    readLines = f.readlines()

for lines in readLines :        # 리스트 형태로 저장된 readLines에서 한 줄씩 한글로 변환하여 출력
    result1 = translator.translate(lines, dest="ko")
    print(result1.text)
    with open(write_file_path, "a", encoding="UTF8") as f :     # 파일 저장, 한글 사용 위해서 UTF8 사용
        f.write(result1.text + "\n")        # \n 줄바꿈 추가
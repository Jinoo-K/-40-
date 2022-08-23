# pip install qrcode

import qrcode   # qrcode 라이브러리 불러오기

file_path = r'4. QR코드 생성기\qr코드모음.txt'
with open(file_path, "rt", encoding="UTF8") as f :   # 4. QR코드 생성기에서 qr코드모음.txt 읽기
    read_lines = f.readlines()      # f.readlines()로 파읽을 읽어 줄 별로 리스트의 값의 형태로 출력
    
    for line in read_lines :
        line = line.strip()
        print(line)
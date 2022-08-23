# pip install qrcode

import qrcode   # qrcode 라이브러리 불러오기

qr_data = "www.naver.com"
qr_img = qrcode.make(qr_data)   # qrcode.make로 이미지 생성

save_path = "4. QR코드 생성기\\" + qr_data + '.png'     # 저장 경로 4. QR코드 생성기에 www.naver.com.png로 저장
qr_img.save(save_path)      # qrcode 저장
# pip install pyautogui
# pip install pyperclip

import pyautogui
import time
import pyperclip

날씨 = ["창원 날씨", "서울 날씨", "춘천 날씨", "부산 날씨"]     # 검색할 지역 리스트로 저장

addr_x = 235        # 주소창 좌표
addr_y = 95
start_x = 51        # 캡쳐할 시작 좌표 및 끝 좌표 설정
start_y = 387
end_x = 1038
end_y = 1005

for 지역날씨 in 날씨 :
    pyautogui.moveTo(addr_x, addr_y)        # 주소창 좌표로 이동
    time.sleep(0.5)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.write("www.naver.com", interval=0.1)      # 네이버 입력 후 엔터키 입력
    pyautogui.write(["Enter"])
    time.sleep(2)

    pyperclip.copy(지역날씨)        # 리스트에서 불러온 지역 날씨 입력
    pyautogui.hotkey("ctrl", "v")
    time.sleep(0.5)
    pyautogui.write(["Enter"])
    time.sleep(2)
    저장경로 = "10. 오토마우스를 활용한 웹페이지 자동화\\" + 지역날씨 + '.png'
    pyautogui.screenshot(저장경로, region=(start_x, start_y, end_x-start_x, end_y-start_y))
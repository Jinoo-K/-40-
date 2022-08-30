# pip install pyautogui
# pip install pyperclip

import pyautogui
import time
import pyperclip

pyautogui.moveTo(480,367)       # 네이버 홈 화면 검색창 좌표로 이동
pyautogui.click()
time.sleep(1)

pyperclip.copy("창원 날씨")
pyautogui.hotkey("ctrl", "v")
time.sleep(1)

pyautogui.write(["Enter"])
time.sleep(2)

start_x = 51        # 캡쳐할 시작 좌표 및 끝 좌표 설정
start_y = 387
end_x = 1038
end_y = 1005

pyautogui.screenshot(r"10. 오토마우스를 활용한 웹페이지 자동화\창원 날씨.png", region=(start_x, start_y, end_x-start_x, end_y-start_y))     # 설정된 좌표로 캡쳐하여 파일 저장
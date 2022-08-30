# pip install pyautogui
# pip install pyperclip

import pyautogui
import time
import pyperclip

pyautogui.moveTo(480,367)       # 네이버 홈 화면 검색창 좌표로 이동
pyautogui.click()
time.sleep(0.5)

pyperclip.copy("창원 날씨")     # 클립보드에 창원 날씨 저장
pyautogui.hotkey("ctrl", "v")       # 검색창에 붙여넣기
time.sleep(0.5)

pyautogui.write(["Enter"])
time.sleep(1)
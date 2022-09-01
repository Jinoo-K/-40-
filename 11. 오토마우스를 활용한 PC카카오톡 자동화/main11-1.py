# pip install pyautogui
# pip install pyperclip
# pip install schedule

import pyautogui
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))        # 경로를 .py 현재 파일의 실행 경로로 이동

picPosition = pyautogui.locateOnScreen("pic1.png")      # pic1.png와 동일한 그림을 찾아 좌표 출력
print(picPosition)

if picPosition is None : 
    picPosition = pyautogui.locateOnScreen("pic2.png")
    
if picPosition is None :
    picPosition = pyautogui.locateOnScreen("pic3.png")
    print(picPosition)
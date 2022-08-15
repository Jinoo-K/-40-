# pip install pyautogui
# pip install pyperclip
# pip install schedule

import pyautogui
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

picPosition = pyautogui.locateOnScreen("pic1.png")
print(picPosition)

if picPosition is None : 
    picPosition = pyautogui.locateOnScreen("pic2.png")
    
if picPosition is None :
    picPosition = pyautogui.locateOnScreen("pic3.png")
    print(picPosition)
# pip install pyautogui
# pip install pyperclip

import pyautogui
import time
import pyperclip

pyautogui.moveTo(480,367)
pyautogui.click()
time.sleep(0.5)

pyperclip.copy("창원 날씨")
pyautogui.hotkey("ctrl", "v")
time.sleep(0.5)

pyautogui.write(["Enter"])
time.sleep(1)
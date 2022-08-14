# pip install pyautogui
# pip install pyperclip

import pyautogui
import time
import pyperclip

pyautogui.moveTo(480,367)
pyautogui.click()
time.sleep(1)

pyperclip.copy("창원 날씨")
pyautogui.hotkey("ctrl", "v")
time.sleep(1)

pyautogui.write(["Enter"])
time.sleep(2)

start_x = 51
start_y = 387
end_x = 1038
end_y = 1005

pyautogui.screenshot(r"10. 오토마우스를 활용한 웹페이지 자동화\창원 날씨.png", region=(start_x, start_y, end_x-start_x, end_y-start_y))
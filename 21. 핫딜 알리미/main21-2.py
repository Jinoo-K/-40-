from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
import telegram
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

send_message_list = []

while True :
    try :
        driver.get(url="https://www.ppomppu.co.kr/zboard/zboard.php?id=ppomppu")
        titles = driver.find_elements(By.CSS_SELECTOR, "#revolution_main_table > tbody > tr > td > table > tbody > tr > td:nth-child(2) > div > a > font")
        urls = driver.find_elements(By.CSS_SELECTOR, "#revolution_main_table > tbody > tr > td > table > tbody > tr > td:nth-child(2) > div > a")
        
        message = ""
        for i in range(len(titles)):
            if "김치" in titles[i].text:
                message = titles[i].text + "\n" + urls[i].get_attribute("href")
                if message not in send_message_list :
                    print(message)
                    send_message_list.append(message)
                    token = ""
                    id = ""
                    bot = telegram.Bot(token)
                    bot.sendMessage(chat_id=id, text=message)
                    
        time.sleep(60.0 * 5)
        
    except :
        break
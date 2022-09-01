#!/usr/bin/env python
# coding: utf-8

# In[5]:


# pip install selenium : 웹을 제어하는 라이브러리
# pip install webdriver-manager

from webdriver_manager.chrome import ChromeDriverManager        # 구글 크롬 드라이버의 설치를 위한 라이브러리
from selenium import webdriver

driver = webdriver.Chrome(ChromeDriverManager().install())      # 크롬 드라이버 시작, 없으면 설치

URL="https://www.google.co.kr/imghp"
driver.get(url=URL)

driver.implicitly_wait(time_to_wait=10)


# In[7]:


from selenium.webdriver.common.keys import Keys

elem = driver.find_element_by_css_selector("#sbtc > div > div.a4bIc > input")       # 셀레니움의 css selector을 통해 원소를 찾음
elem.send_keys("바다")
elem.send_keys(Keys.RETURN)


# In[8]:


import time
elem = driver.find_element_by_tag_name("body")
for i in range(60):
    elem.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.1)
    
try:
    driver.find_element_by_css_selector("islmp > div > div > div > div.gBPM8 > div.qvfT1 > div.YstHxe > input").click()     # 결과더보기 버튼이 있다면 눌러서 사진 더 나오게
    
    for i in range(60):
        elem.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.1)
        
except:
    pass


# In[ ]:


links=[]
images = driver.find_elements_by_css_selector("#islrg > div.islrc > div > a.wXeWr.islib.nfEiy > div.bRMDJF.islir > img")        # 이미지의 원소를 모두 찾음

for image in images :
    if image.get_attribute("src") is not None :
        links.append(image.get_attribute("src"))
        
print("찾은 이미지 개수 :", len(links))


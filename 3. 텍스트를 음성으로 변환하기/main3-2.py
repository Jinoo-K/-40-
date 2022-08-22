# pip install gtts

from gtts import gTTS    #gtts 라이브러리 안에 gTTS 불러오기
from playsound import playsound    # playsoun 라이브러리 안에서 playsound 불러오기
import os    # 경로 이동 위해서 os 라이브러리 불러오기

os.chdir(os.path.dirname(os.path.abspath(__file__)))    # playsound에서 한글 인식 못함. 경로를 이 프로그램으로 이동

text = "안녕하세요. 김진우입니다."

tts = gTTS(text = text, lang='ko')    # text 변수의 문자열을 ko(한글)로 변환하여 tts에 바인딩
tts.save("hi.mp3")

playsound("hi.mp3")    # hi.mp3 재생
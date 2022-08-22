# pip install gtts

from gtts import gTTS    #gtts 라이브러리 안에 gTTS 불러오기
from playsound import playsound    # playsoun 라이브러리 안에서 playsound 불러오기
import os    # 경로 이동 위해서 os 라이브러리 불러오기

os.chdir(os.path.dirname(os.path.abspath(__file__)))    # playsound에서 한글 인식 못함. 경로를 이 프로그램으로 이동

file_path = "나의텍스트.txt"    # 나의텍스트.txt 경로 변수
with open(file_path, 'rt', encoding = "UTF8") as f:    # f로 파일 열기, 한글로 작성된 파일을 열기 때문에 'rt', encoindg="UTF8", with는 파일을 열고 종료되면 자동으로 파일을 닫음
    read_file = f.read()    # read_file = 파일 읽기
    
tts = gTTS(text = read_file, lang='ko')
tts.save("myText.mp3")

playsound("myText.mp3")
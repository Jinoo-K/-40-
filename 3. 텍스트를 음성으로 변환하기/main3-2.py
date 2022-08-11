from winsound import PlaySound
from gtts import gTTS
from playsound import playsound
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

text = "안녕하세요. 김진우입니다."

tts = gTTS(text = text, lang='ko')
tts.save("hi.mp3")

playsound("hi.mp3")
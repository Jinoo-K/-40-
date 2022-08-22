# pip install gtts

from gtts import gTTS    #gtts 라이브러리 안에 gTTS만 불러오기

text = "안녕하세요. 깅지누입니다."

tts = gTTS(text = text, lang='ko')    # text 변수의 문자열을 ko(한글)로 변환하여 tts에 바인딩
tts.save(r"3. 텍스트를 음성으로 변환하기\hi.mp3")    # 문자열 앞에 r을 넣어주면 \를 특별한 명령어로 인식하지 않고 역슬래쉬 자체로 해석
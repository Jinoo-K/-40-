from gtts import gTTS

text = "안녕하세요. 깅지누입니다."

tts = gTTS(text = text, lang='ko')
tts.save(r"3. 텍스트를 음성으로 변환하기\hi.mp3")
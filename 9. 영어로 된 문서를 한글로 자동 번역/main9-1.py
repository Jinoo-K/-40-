# pip install googletrans==4.0.0-rc1

import googletrans      # googletrans 모듈 불러오기

translator = googletrans.Translator()

str1 = "행복하세요"     # "행복하세요"를 영어로 번역, dest에는 번역될 문자 입력, src에는 번역할 문자의 언어 (기본값이 auto)
result1 = translator.translate(str1, dest="en", src="auto")
print(f"행복하세요 => {result1.text}")

str2 = "I am happy"     # "I am happy"를 한글로 번역, dest에는 번역될 문자 입력, stc에서는 번역할 문자의 언어
result2 = translator.translate(str2, dest="ko", src="en")
print(f"I am happy => {result2.text}")
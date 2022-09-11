# pip install python-telegram-bot

import telegram

token = ""
id = ""

bot = telegram.Bot(token)
bot.sendMessage(chat_id=id, text="파이썬을 보내는 메세지입니다.")
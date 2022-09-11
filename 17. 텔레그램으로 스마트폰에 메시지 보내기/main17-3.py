# pip install python-telegram-bot

from asyncore import dispatcher
import telegram
from telegram.ext import Updater
from telegram.ext import MessageHandler, Filters

token = ""
id = ""

bot = telegram.bot(token)
bot.sendMessage(chat_id=id, text="자동응답 테스트입니다. 안녕 또는 뭐해를 입력해보세요.")

updater = Updater(token=token, use_context=True)
dispatcher = updater.dispatcher
updater.start_polling()

def handler(update, context) :
    user_text = update.message.text
    if user_text == "안녕" :
        bot.send_message(chat_id = id, text="응, 안녕")
    elif user_text == "뭐해" :
        bot.send_message(chat_id = id, text="그냥 있지")

echo_handler = MessageHandler(Filters.text, handler)
dispatcher.add_handler(echo_handler)
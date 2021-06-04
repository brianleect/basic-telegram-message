# Import telegram library
import telegram as telegram
from constants import token,chat_id

bot = telegram.Bot(token=token)

def send_message(message):
    bot.send_message(chat_id=chat_id,text=message)

send_message("Hello")
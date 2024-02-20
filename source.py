import telebot
from math import *

bot = telebot.TeleBot('Здесь нужен ключ')

@bot.message_handler(commands=['start'])
def handle_text(message):
    numvan = bot.send_message(message.chat.id, 'Введите выражение')
    bot.register_next_step_handler(numvan ,operi)

def operi(message):
    bot.send_message(message.chat.id,eval(message.text))

bot.polling(none_stop=True)

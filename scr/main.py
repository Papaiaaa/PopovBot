import telebot
from telebot import types

import config
TOKEN =config.TOKEN1

bot=telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    btn1 = types.KeyboardButton('Резюме')
    btn2 = types.KeyboardButton('Образование')
    btn3 = types.KeyboardButton('Обо мне')
    markup.add(btn1,btn2,btn3)
    greetings = f'Привет, <b>{message.from_user.first_name} {message.from_user.last_name}</b>'
    bot.send_message(message.chat.id, greetings, parse_mode='html', reply_markup=markup)



bot.polling(none_stop=True)
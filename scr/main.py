import telebot
from telebot import types

import config
TOKEN =config.TOKEN1

bot=telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    btn1 = types.KeyboardButton('Не знаю с чего начать')
    btn2 = types.KeyboardButton('Выбор сотового оператора')
    btn3 = types.KeyboardButton('Оформление медицинской страховки')
    btn4 = types.KeyboardButton('Получить Турецкий ИНН')
    btn5 = types.KeyboardButton('Документы для ВНЖ')
    btn6 = types.KeyboardButton('Как открыть счет в банке')
    btn7 = types.KeyboardButton('Сервисы по доставке')
    btn8 = types.KeyboardButton('Ремонт компьютеров')
    btn9 = types.KeyboardButton('Telegram канал')
    markup.add(btn1,btn2,btn3,btn4,btn5,btn6,btn7,btn8,btn9)
    greetings = f'Привет, <b>{message.from_user.first_name} {message.from_user.last_name}</b>'
    bot.send_message(message.chat.id, greetings, parse_mode='html', reply_markup=markup)
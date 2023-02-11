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
    greetings = f'Привет, <b>{message.from_user.first_name} {message.from_user.last_name}</b>\nПожалуйста, воспользутесь навигацией ниже:'
    bot.send_message(message.chat.id, greetings, parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def mess(message):
    get_message_bot = message.text.strip().lower()
    if get_message_bot == "резюме":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('Вывести на экран')
        btn2 = types.KeyboardButton('Скачать CV')
        markup.add(btn1, btn2)
        final_message = "Выбери один из вариантов ниже:"
        bot.send_message(message.chat.id, final_message, reply_markup=markup)

    elif get_message_bot == "образование":
        final_message = 'тусур тгу'
        bot.send_message(message.chat.id, final_message, parse_mode='html')
    elif get_message_bot == "обо мне":
        final_message = '123'
        bot.send_message(message.chat.id, final_message, parse_mode='html')
bot.polling(none_stop=True)
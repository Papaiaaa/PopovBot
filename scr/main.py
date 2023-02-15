import telebot
from telebot import types


from datetime import datetime

import config
TOKEN =config.TOKEN1

import pyperclip

import about
about_message = about.about_txt

import edu
tusur = edu.edu1_txt
tsu = edu.edu2_txt
netology = edu.edu3_txt

import contacts
contact_message = contacts.contact

bot=telebot.TeleBot(TOKEN)
current_datetime = str(datetime.now())
@bot.message_handler(content_types=["sticker"])
def send_sticker(message):
    sticker_id = message.sticker.file_id
    bot.send_message(message.chat.id, sticker_id)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    btn1 = types.KeyboardButton('Резюме')
    btn2 = types.KeyboardButton('Образование')
    btn3 = types.KeyboardButton('Обо мне')
    btn4 = types.KeyboardButton('Контакты')
    markup.add(btn1,btn2,btn3,btn4)
    greetings = f'Привет, <b>{message.from_user.first_name} {message.from_user.last_name}</b>\nПожалуйста, воспользутесь навигацией ниже:'
    bot.send_message(message.chat.id, greetings, parse_mode='html', reply_markup=markup)

@bot.message_handler(commands=['education'])
def education(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    btn1 = types.KeyboardButton('ТУСУР `11')
    btn2 = types.KeyboardButton('ТГУ `15')
    btn3 = types.KeyboardButton('Нетология `22')
    markup.add(btn1, btn2, btn3)
    final_message = "Выбери один из вариантов ниже:"
    bot.send_message(message.chat.id, final_message, reply_markup=markup)
@bot.message_handler(commands=['about'])
def about(message):
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIBBGPstpI2hketg-noGW2wYZZs9fxfAALPIgACbKNpS3eQe7GdYF-_LgQ')
    bot.send_message(message.chat.id, about_message, parse_mode='html')

@bot.message_handler(commands=['contacts'])
def contacts(message):
    bot.send_message(message.chat.id, contact_message, parse_mode='html')

@bot.message_handler(commands=['callme'])
def callme(message):
    usder = message.from_user.username
    print(usder)
    print(current_datetime)
    my_file = open("scr\who.txt", "a")
    my_file.write('@' + message.from_user.username + ' ' + current_datetime + '\n')
    my_file.close()
    call_message = "В близжайшее время с Вами свяжутся"
    bot.send_message(message.chat.id, call_message, parse_mode='html')
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
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('ТУСУР `11')
        btn2 = types.KeyboardButton('ТГУ `15')
        btn3 = types.KeyboardButton('Нетология `22')
        markup.add(btn1, btn2, btn3)
        final_message = "Выбери один из вариантов ниже:"
        bot.send_message(message.chat.id, final_message, reply_markup=markup)

        #bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIBBmPstpQHEeNaYTHHLqFrmY8Qq9TyAAJ2JgACS_FpS54nHFUr5pb2LgQ')
        #bot.send_message(message.chat.id, tusur, parse_mode='html')
        #bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIBCGPstpbYl_UtFaG0o_Zkyb-WCRrAAAIeJgAChORpSz8_zuUFfdC6LgQ')
        #bot.send_message(message.chat.id, tsu, parse_mode='html')
        #bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIBCmPstpi9WSMamGXvm4H4dZ39EgOWAAJhJgACJ01hS15tjpWCfVRELgQ')
        #bot.send_message(message.chat.id, netology, parse_mode='html')
    elif get_message_bot == "обо мне":
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIBBGPstpI2hketg-noGW2wYZZs9fxfAALPIgACbKNpS3eQe7GdYF-_LgQ')
        bot.send_message(message.chat.id, about_message, parse_mode='html')

    elif get_message_bot == "тусур `11":
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIBBmPstpQHEeNaYTHHLqFrmY8Qq9TyAAJ2JgACS_FpS54nHFUr5pb2LgQ')
        bot.send_message(message.chat.id, tusur, parse_mode='html')
    elif get_message_bot == "тгу `15":
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIBCGPstpbYl_UtFaG0o_Zkyb-WCRrAAAIeJgAChORpSz8_zuUFfdC6LgQ')
        bot.send_message(message.chat.id, tsu, parse_mode='html')
    elif get_message_bot == "нетология `22":
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAICN2Ps_Hk-5KQSleM2IZPnHn0jt2i_AAI_JAAC0KlpS55w2_0wCx3dLgQ')
        bot.send_message(message.chat.id, netology, parse_mode='html')
    elif get_message_bot == "контакты":
        bot.send_message(message.chat.id, contact_message, parse_mode='html')
bot.polling(none_stop=True)
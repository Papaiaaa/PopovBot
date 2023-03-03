import time
from email import message

import requests
import telebot
from telebot import types


from datetime import datetime

from telebot.types import KeyboardButton

import config
TOKEN =config.TOKEN1

import pyperclip

import about
about_message = about.about_txt
import exp
exp_message = exp.exp_txt
exp_ase_message = exp.exp_ase_txt
exp_contek_message = exp.exp_contek_txt
exp_it_message = exp.exp_it_txt
exp_all_message = exp_message + exp_ase_message + exp_it_message + exp_contek_message
#print(exp_all_message)
import edu
tusur = edu.edu1_txt
tsu = edu.edu2_txt
netology = edu.edu3_txt

import contacts
contact_message = contacts.contact
import kb
markup1 = kb.markup
markup2 = kb.markup2
markup3 = kb.markup3
markup4 = kb.markup4
markup5 = kb.markup5


bot=telebot.TeleBot(TOKEN)
current_datetime = str(datetime.now())

@bot.message_handler(content_types=["sticker"])
def send_sticker(message):
    sticker_id = message.sticker.file_id
    bot.send_message(message.chat.id, sticker_id)

@bot.message_handler(commands=['start'])
def start(message):
    #markup = types.ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton('Отправить свой контакт ☎️', request_contact=True)).add(KeyboardButton('Резюме', request_contact=True)).add(KeyboardButton('Резюме', request_contact=True)).add(KeyboardButton('Резюме', request_contact=True))
    greetings = f'Привет, <b>{message.from_user.first_name} {message.from_user.last_name}</b>\nПожалуйста, воспользутесь навигацией ниже:'
    bot.send_message(message.chat.id, greetings, parse_mode='html', reply_markup=markup1)

@bot.message_handler(commands=['education'])
def education(message):
    final_message = "Выбери один из вариантов ниже:"
    bot.send_message(message.chat.id, final_message, reply_markup=markup2)
@bot.message_handler(commands=['about'])
def about(message):
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIBBGPstpI2hketg-noGW2wYZZs9fxfAALPIgACbKNpS3eQe7GdYF-_LgQ')
    bot.send_message(message.chat.id, about_message, parse_mode='html')

@bot.message_handler(commands=['contacts'])
def contacts(message):
    bot.send_message(message.chat.id, contact_message, reply_markup=markup3,  parse_mode='html')

@bot.message_handler(commands=['cv'])
def contacts(message):
    final_message = "Выбери один из вариантов ниже:"
    bot.send_message(message.chat.id, final_message, reply_markup=markup4,  parse_mode='html')
@bot.message_handler(commands=['callme'])
def callme(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    btn1 = types.KeyboardButton('Обратная свзяь')
    markup.add(btn1)
    usder = message.from_user.username
    message.from_user.first_name = str(message.from_user.first_name)
    message.from_user.last_name = str(message.from_user.last_name)
    print(usder)
    print(current_datetime)
    my_file = open("scr\who.txt", "a")
    my_file.write('@' + message.from_user.username + ' ' + current_datetime + '\n')
    my_file.close()
    url = 'https://api.telegram.org/bot5828319410:AAGeWWFB9UV_tUmyyw6RQ6dm_cINQRL-Aa4/sendMessage?chat_id=145845542&text=С Вами хочет свзяаться @'+ usder +' . Что ему нужно?'
    #headers = {'ContentType': 'application/vnd.api+json', 'X-Auth-Token': token}
    response = requests.get(url=url)
    print(response.json())
    #
    call_message = "В ближайшее время с Вами свяжутся"
    bot.send_message(message.chat.id, call_message, reply_markup=markup, parse_mode='html')
@bot.message_handler(content_types=['text'])
def mess(message):
    get_message_bot = message.text.strip().lower()
    if get_message_bot == "резюме":
        final_message = "Выбери один из вариантов ниже:"
        bot.send_message(message.chat.id, final_message, reply_markup=markup4)

    elif get_message_bot == "образование":
        final_message = "Выбери один из вариантов ниже:"
        bot.send_message(message.chat.id, final_message, reply_markup=markup2)

    elif get_message_bot == "обо мне":
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIBBGPstpI2hketg-noGW2wYZZs9fxfAALPIgACbKNpS3eQe7GdYF-_LgQ')
        bot.send_message(message.chat.id, about_message, parse_mode='html')
    elif get_message_bot == "вывести на экран":
        usder = message.from_user.username
        message.from_user.first_name = str(message.from_user.first_name)
        message.from_user.last_name = str(message.from_user.last_name)
        url = 'https://api.telegram.org/bot5828319410:AAGeWWFB9UV_tUmyyw6RQ6dm_cINQRL-Aa4/sendMessage?chat_id=145845542&text=Пользователь @' + usder +' ' + message.from_user.first_name +' '+ message.from_user.last_name +' нажал кнопку Вывести на экран CV'
        response = requests.get(url=url)
        print(response.json())
        final_message = "Выбери один из вариантов ниже:"
        bot.send_message(message.chat.id, final_message, reply_markup=markup5)
        #bot.send_message(message.chat.id, exp_message, parse_mode='html')
    elif get_message_bot == "газпром инвест томск `22":
        bot.send_message(message.chat.id, exp_message, parse_mode='html')
    elif get_message_bot == "атомстройэкспорт в нр бангладеш `19":
        bot.send_message(message.chat.id, exp_ase_message, parse_mode='html')
    elif get_message_bot == "зао айти `15":
        bot.send_message(message.chat.id, exp_it_message, parse_mode='html')
    elif get_message_bot == "ооо контек-софт `15":
        bot.send_message(message.chat.id, exp_contek_message, parse_mode='html')
    elif get_message_bot == "вывести всю информацию":
        bot.send_message(message.chat.id, exp_all_message, parse_mode='html')
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
        bot.send_message(message.chat.id, contact_message, reply_markup=markup3, parse_mode='html')
    elif get_message_bot == "скачать cv":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Скачать", url="https://hh.ru/resume_converter/%D0%9F%D0%BE%D0%BF%D0%BE%D0%B2%20%D0%A0%D0%BE%D0%BC%D0%B0%D0%BD.pdf?hash=e12743f0ff0b7bcfee0039ed1f573469477765&type=pdf&hhtmSource=resume&hhtmFrom=resume_list"))
        bot.send_message(message.chat.id, 'Резюме', parse_mode='html', reply_markup=markup)
    elif get_message_bot == "главное меню":
        greetings = f'Пожалуйста, воспользутесь навигацией ниже:'
        bot.send_message(message.chat.id, greetings, parse_mode='html', reply_markup=markup1)
    elif get_message_bot == "обратная связь":
        usder = str(message.from_user.username)
        message.from_user.first_name = str(message.from_user.first_name)
        message.from_user.last_name = str(message.from_user.last_name)
        print(usder)
        print(current_datetime)
        print(message.from_user.first_name)
        print(message.from_user.last_name)
        my_file = open("scr\who.txt", "a")
        my_file.write('@' + message.from_user.username + ' ' + current_datetime + '\n')
        my_file.close()
        url = 'https://api.telegram.org/bot5828319410:AAGeWWFB9UV_tUmyyw6RQ6dm_cINQRL-Aa4/sendMessage?chat_id=145845542&text=С Вами хочет связаться @'+ usder +' ' + message.from_user.first_name +' '+ message.from_user.last_name +'. Что ему нужно?'
    #headers = {'ContentType': 'application/vnd.api+json', 'X-Auth-Token': token}
        response = requests.get(url=url)
        print(response.json())
        call_message = "В ближайшее время с Вами свяжутся"
        bot.send_message(message.chat.id, call_message, parse_mode='html')
#bot.polling(none_stop=True)

while True:
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(e)
        time.sleep(15)
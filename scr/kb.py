import telebot
from telebot.types import ReplyKeyboardMarkup

markup: ReplyKeyboardMarkup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = telebot.types.KeyboardButton('Резюме')
btn2 = telebot.types.KeyboardButton('Образование')
btn3 = telebot.types.KeyboardButton('Обо мне')
btn4 = telebot.types.KeyboardButton('Контакты')
#btn5 = telebot.types.KeyboardButton('TEST')
#btn6 = telebot.types.KeyboardButton('TEST2')
markup.add(btn1, btn2, btn3)
markup.add(btn4)
#markup.add(btn6)

markup2: ReplyKeyboardMarkup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
btn1 = telebot.types.KeyboardButton('ТУСУР `11')
btn2 = telebot.types.KeyboardButton('ТГУ `15')
btn3 = telebot.types.KeyboardButton('Нетология `22')
btn4 = telebot.types.KeyboardButton('Главное Меню')
markup2.add(btn1, btn2, btn3, btn4)

markup3: ReplyKeyboardMarkup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
btn1 = telebot.types.KeyboardButton("Обратная связь")
btn2 = telebot.types.KeyboardButton('Главное Меню')
markup3.add(btn1, btn2)

markup4: ReplyKeyboardMarkup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
btn1 = telebot.types.KeyboardButton('Вывести на экран')
btn2 = telebot.types.KeyboardButton('Скачать CV')
btn3 = telebot.types.KeyboardButton('Главное Меню')
markup4.add(btn1, btn2, btn3)
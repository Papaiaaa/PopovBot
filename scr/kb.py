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
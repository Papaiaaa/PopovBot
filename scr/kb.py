import telebot
from telebot.types import ReplyKeyboardMarkup

markup: ReplyKeyboardMarkup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = telebot.types.KeyboardButton('Резюме')
btn2 = telebot.types.KeyboardButton('Образование')
btn3 = telebot.types.KeyboardButton('Обо мне')
btn4 = telebot.types.KeyboardButton('Контакты')
markup.add(btn1, btn2, btn3)
markup.add(btn4)

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

markup5: ReplyKeyboardMarkup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
btn1 = telebot.types.KeyboardButton('Газпром Инвест Томск `22')
btn2 = telebot.types.KeyboardButton('АтомСтройЭкспорт в НР Бангладеш `19')
btn3 = telebot.types.KeyboardButton('ЗАО АйТи `15')
btn4 = telebot.types.KeyboardButton('ООО Контек-Софт `15')
btn5 = telebot.types.KeyboardButton('Вывести всю информацию')
btn6 = telebot.types.KeyboardButton('Главное Меню')
markup5.add(btn1, btn2, btn3, btn4)
markup5.add(btn5)
markup5.add(btn6)
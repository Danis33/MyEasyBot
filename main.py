import telebot
import os

from dotenv import load_dotenv
from telebot import types

load_dotenv()

bot = telebot.TeleBot(os.getenv('TOKEN'))


@bot.message_handler(commands=['info'])
def info_user(message):
    markup = types.InlineKeyboardMarkup()
    menu1 = types.InlineKeyboardButton('Назад', callback_data='/menu')
    markup.add(menu1)
    bot.send_message(
        message.chat.id,
        f'Имя пользователя: {message.chat.first_name}\n'
        f'Псевдоним пользователя: {message.chat.username}\n'
        f'ID пользователя: {message.chat.id}\n',
        reply_markup=markup
    )


@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.message:
        if callback.data == '/menu':
            bot.send_message(callback.message.chat.id, 'Вы вернулись назад к меню')


@bot.message_handler(commands=['weather'])
def weather(message):
    bot.send_message(
        message.chat.id,
        'Напиши название города в котором хочешь узнать погоду: '
    )


@bot.message_handler()
def start(message):
    if message.text == '/start':
        bot.send_message(
            message.chat.id,
            'Привет, рад тебя видеть на нашем сервере.\n'
            'Если вы тут в первые, то обращаитесь за помощью /help\n'
            'Открыть меню /menu\n'
        )

    elif message.text == '/help':
        bot.send_message(
            message.chat.id,
            'Что бы начать напиши /start\n'
        )

    elif message.text == '/menu':
        bot.send_message(
            message.chat.id,
            'Информация о пользователе /info\n'
            'Узнать погоду /weather\n'
        )

    else:
        bot.send_message(
            message.chat.id,
            'Я вас не понимаю. Обратиться за помощью /help'
        )


bot.polling(non_stop=True, interval=0)

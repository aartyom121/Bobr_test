import requests
import telebot
import json

bot = telebot.TeleBot('7133165979:AAGu_hePpN6BMjRi64Fes99BDJalEZbQDtg')
API = '5bf1bd9cce67821d6e086103698e721d'


@bot.message_handler(commands=['start'])
def start_bot(message):
    if message.from_user.last_name and message.from_user.first_name:
        first_message = (f"Привет, <b>{message.from_user.first_name} {message.from_user.last_name}!</b>\n"
                         f"Введи название своего города.")
    else:
        first_message = (f"Привет, <b>{message.from_user.first_name}!</b>\n"
                         f"Введи название своего города.")
    bot.send_message(message.chat.id, first_message, parse_mode="html")


@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.lower()
    try:
        data_json = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric&lang=ru")
        data = json.loads(data_json.text)

        bot.reply_to(message, f"Температура: {int(data['main']['temp'])}°С\n"
                              f"Ощущается как: {int(data['main']['feels_like'])}°С\n"
                              f"Влажность: {data['main']['humidity']}%\n"
                              f"Описание: {data['weather'][0]['description']}")
    except Exception as e:
        bot.reply_to(message, f'Ошибка: {str(e)}. Пожалуйста, повторите позже.')


bot.infinity_polling()

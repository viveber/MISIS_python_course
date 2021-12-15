import telebot
from telebot import types
import requests
from requests.exceptions import HTTPError

bot = telebot.TeleBot('тут должен быть токен')

@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, ' Привет! Я бот для проверки доступности сайтов. Введи адрес сайта (url). \nЛибо напиши /help.')

# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
	if message.text == "/help":
		bot.send_message(message.from_user.id, "Адрес сайта нужно вводить в формате: 'xxxxx.xxx' \nНапример, google.com \nПопробуй!")

	else:
		bot.send_message(message.chat.id, 'Уже проверяю... ' + message.text)
		res = url_check(message.text)
		bot.send_message(message.chat.id, res)

def url_check(url_input): 
    for url in [f'http://{url_input}']:
        try:
            response = requests.get(url)
            response.raise_for_status()
        except HTTPError as http_err:
            result = f'Вышла вот такая HTTP-ошибка: {http_err}'
            return result
        except Exception as err:
            result = f'Обнаружена какая то ошибка: {err}'
            return result
        else:
            result = 'Успех! Сайт доступен'
            return result

bot.polling(none_stop=True, interval=0)

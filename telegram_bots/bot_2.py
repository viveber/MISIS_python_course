import telebot
from telebot import types
import pymorphy2

bot = telebot.TeleBot('тут должен быть токен')

@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, ' Привет! Я бот для анализа текста, который ты мне пришлёшь.\nСтатистика такая:\n1. количество уникальных слов\n2. самое популярное слово (кроме союзов и предлогов)\n3. количество предложений\nДля помощи напиши /help.')

# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
	if message.text == "/help":
		bot.send_message(message.from_user.id, "Слушай, ну вроде и так всё понятно, просто пришли мне какой нибудь текст. Я посчитаю всё и напишу тебе ответ...")

	else:
		bot.send_message(message.chat.id, 'Анализирую... ')
		res = text_analyzer(message.text)
		bot.send_message(message.chat.id, res)

def extra_parts(word, morth=pymorphy2.MorphAnalyzer()):
        return morth.parse(word)[0].tag.POS

def text_analyzer(text): 
    words = text.lower().split()
    most_used = ''
    count_word = 0
    unique_words = ''
    number_of_sentences = text.count('.')+text.count('!')+text.count('?')

# удаление символов
    for word in words:
        for symbol in word:
            if symbol in '!@#$%^&*()_+-="[{]}\|/?.>,<№;:':
                word.replace(symbol, '')
    unique_words = len(words)

# удаление предлогов и союзов из списка слов 
    extras = {'INTJ', 'PRCL', 'CONJ', 'PREP'}
    words = [word for word in words if extra_parts(word) not in extras]

    for word in words:
        if words.count(word) > count_word and word not in []:
            count_word = words.count(word)
            most_used = word
    return f'Статистика по тексту:\nКоличество уникальных слов - {unique_words}\nСамое популярное слово - {most_used}\nКоличество предложений - {number_of_sentences}'

bot.polling(none_stop=True, interval=0)



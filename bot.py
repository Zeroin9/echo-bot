# Simple echobot for telegram with pyTelegramBotAPI
import time
import telebot
from telebot import types

bot_token = '';

# Settings variables
with open('settings.txt', 'r') as reader:
    bot_token = reader.readline().strip()

# Create a bot variable and remove old webhook
bot = telebot.TeleBot(bot_token)
bot.remove_webhook()
time.sleep(1)

@bot.message_handler(commands=['start'])
def startCommand(message):
    print('recieve START from', message.chat.id)
    bot.send_message(message.chat.id, 'Hi *' + message.chat.first_name + '*!', parse_mode='Markdown', reply_markup=types.ReplyKeyboardRemove())

@bot.message_handler(func=lambda message: True, content_types=['text'])
def simple_echo(message):
    print('recieve message:', message.text, '\nfrom', message.chat.id)
    bot.send_message(message.chat.id, message.text, parse_mode='Markdown', reply_markup=types.ReplyKeyboardRemove())

print('bot start')
bot.polling()
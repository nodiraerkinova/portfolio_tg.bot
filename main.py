import telebot
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(TOKEN, parse_mode=None)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Assalomu alekum, botimizga xush kelibsiz!")


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    print(message.text)
    text = message.text
    if text.isascii():
        bot.reply_to(message, text)
    else:
        bot.reply_to(message, text)


bot.polling()
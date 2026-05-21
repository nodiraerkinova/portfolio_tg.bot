import telebot
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(TOKEN, parse_mode=None)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Assalomu alekum, botimizga xush kelibsiz!")

@bot.message_handler(commands=['about'])
def send_about(message):
    bot.reply_to(message, "Bu bot Telebot kutubxonasi yordamida yaratilgan.")

@bot.message_handler(commands=["help"])
def help_cmd(message):
    text = (
        "📋 <b>Mavjud buyruqlar:</b>\n\n"
        "/about — Men haqimda\n"
        "/skills — Ko'nikmalarim\n"
        "/projects — Loyihalarim\n"
        "/contact — Bog'lanish ma'lumotlari\n"
        "/cv — CV ni ko'rish\n"
        "/github — GitHub profil\n"
    )
    bot.send_message(message.chat.id, text, parse_mode="HTML")



bot.polling()
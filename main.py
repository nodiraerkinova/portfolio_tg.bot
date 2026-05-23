import telebot
from telebot import types 
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(TOKEN, parse_mode=None)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    # bot.reply_to(message, "Assalomu alekum, botimga xush kelibsiz!")
    text = "Assalomu alekum, meni potrtfolio botimga xush kelibsiz! Quyidagi tugmalardan birini tanlang:"
    keyboard = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton("About me")
    btn2 = types.KeyboardButton("Contact")
    btn3 = types.KeyboardButton("Projects")
    btn4 = types.KeyboardButton("Skills")
    keyboard.add(btn1, btn2)
    keyboard.add(btn3, btn4)
    bot.send_message(message.chat.id, text, reply_markup=keyboard)


# @bot.message_handler(func=lambda message: True)
# def echo_all(message):
#     if message.text == "About me":
#         bot.send_message(message.chat.id, "Men Nodira Erkinova. \n Men dasturchi qizman!")
#     elif message.text == "Contact":
#         bot.send_message(message.chat.id, "Mening emailim: erkinova0924@gnail.com \n Mening telefon raqamim: +998 90 123 45 67")

@bot.message_handler(func=lambda message: message.text == "About me")
def aboutme_handlar(message):
   bot.send_message(message.chat.id, 
    "👩‍💻 Men haqimda:\n\n"
    "Ismim: Nodira Erkinova\n"
    "Kasb: Dasturchi\n"
    "Ko'nikmalar: Python, Web Development\n"
    "Maqsad: Zamonaviy texnologiyalar orqali foydali loyihalar yaratish"
)

@bot.message_handler(func=lambda message: message.text == "Contact")
def contact_handler(message):
    text = "Men bilan bog'lanish uchun pastdagi linklarga bosing"

    keyboard = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("Telegram", url="https://t.me/erkinova0924")
    keyboard.add(btn1)
    btn2 = types.InlineKeyboardButton("GitHub", url="https://github.com/nodiraerkinova")
    keyboard.add(btn2)
    bot.send_message(message.chat.id, text, reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text == "Skills")
def skills_handler(message):
    bot.send_message(message.chat.id,
    "💻 Mening ko'nikmalarim:\n\n"
    "Python\n"
    "Web Development\n"
    "Database Management\n"
    "Problem Solving"
)

@bot.message_handler(func=lambda message: message.text == "Projects")
def projects_handler(message):
    bot.send_message(message.chat.id,
    "📁 Mening loyihalarim:\n\n"
    "1. Portfolio Website\n"
    "2. To-Do List App\n"
    "3. Chat Application"
)

bot.infinity_polling()

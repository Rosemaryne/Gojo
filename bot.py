from config import TOKEN
import telebot
from random import choice
# print(config.TOKEN)

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\\
Hi there, I am Satoru Gojo.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\\
""")

@bot.message_handler(commands=['coin'])
def coin_handler(message):
    coin = choice(["ОРЕЛ", "РЕШКА"])
    bot.reply_to(message, coin)


@bot.message_handler(commands=['joke'])
def coin_handler(message):
    joke = choice(["My boss told me to have a good day. So, I went home."])
    bot.reply_to(message, joke)


@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)

bot.infinity_polling()
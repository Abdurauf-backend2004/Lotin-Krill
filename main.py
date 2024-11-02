from transliterate import to_latin, to_cyrillic
import telebot

TOKEN = '7392312911:AAFpDhU2hx70hH2jxuugbnQDKnSVBvnptnU'
bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    javob = 'Assalomu alaykum, Xush kelibsiz'
    javob += '\nMatn kiriting:'
    bot.reply_to(message, javob)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    msg = message.text
    if msg.isascii():
        javob = to_cyrillic(msg)
    else:
        javob = to_latin(msg)
    bot.reply_to(message, javob)  # Bu yerda javobni qaytaramiz

bot.polling()
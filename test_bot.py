import telebot
import sqlite3

token = '7138566473:AAEKWkly5tVoiRgRXWhMKUWPuHD-uh5NUJY'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    conn = sqlite3.connect('bot_komron.db')
    cour = conn.cursor()

    cour.execute('''CREATE TABLE IF NOT EXISTS user (id INTEGER name varchar(50), passvord varchar(50));''')
    conn.commit()
    cour.close()
    bot.send_message(message.chat.id, "username kiriting")
    bot.register_next_step_handler(message, user_name)


name = ""


def user_name(message):
    global name
    name = message.text.strip()
    bot.send_message(message.chat.id, "parol kiriting")

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

def hello():
    pass

def ismoil_func():
    pass

def user_name(message):
    global name
    name = message.text.strip()
    bot.send_message(message.chat.id, "parol kiriting")


def user_password(messaga):
    password = messaga.text.strip()
    coon = sqlite3.connect("test2.db")
    cur = coon.cursor()
    data = (f"{name}", f"{password}")
    cur.execute(f"INSERT INTO user(name, password) VALUES {data}")
    coon.commit()
    cur.close()
    coon.close()
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton("userlar ruyxati", callback_data="user"))
    bot.send_message(messaga.chat.id, "Ruyxatdan utildi!", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    conn = sqlite3.connect("test2.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM user")
    users = cur.fetchall()
    info = ""
    for el in users:
        info += f"ism {el[1]} Parol {el[2]}"


print("The bot is running...")
bot.polling(non_stop=True)

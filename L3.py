from replit import db
import os
import telebot

token = os.getenv("token")

bot = telebot.TeleBot(token)

db["users"] = {}


def in_or_not(id):
    for i in db["users"].values():
        if id in i:
            return True
        else:
            return False


@bot.message_handler(commands=["start"])
def start(message):
    fullname = message.from_user.first_name + message.from_user.last_name
    username = message.from_user.username
    id = message.from_user.id
    Num = len(db["users"]) + 1
    Myid = 5507902534
    if Myid != id:
        if in_or_not(id) == False:
            db["users"][Num] = [fullname, username, id, Num, Myid]
            db["users"][id] = {
                db["users"].update(
                    {f"user{Num}":

                         [fullname, username, id]
                     }
                )

            bot.polling()

from flask import Flask, request
import telepot
import json
import urllib3
from API import API # bot API
from dbhelper import DBHelper # import class and method created to work with sqlite3

TOKEN = API
db = DBHelper()
URL = "https://api.telegram.org/bot{}/".format(TOKEN)

proxy_url = "http://proxy.server:3128"
telepot.api._pools = {
    'default': urllib3.ProxyManager(proxy_url=proxy_url, num_pools=3, maxsize=10, retries=False, timeout=10),
}
telepot.api._onetime_pool_spec = (urllib3.ProxyManager, dict(proxy_url=proxy_url, num_pools=1, maxsize=1, retries=False, timeout=30))

secret = "C4sC4DuR4S4G4Z"
bot = telepot.Bot(TOKEN)
bot.setWebhook("https://FelipeBarros.pythonanywhere.com/{}".format(secret), max_connections=1)

app = Flask(__name__)

@app.route('/{}'.format(secret), methods=["POST"])
def telegram_webhook():
    update = request.get_json()
    if "message" in update:
        text = update["message"]["text"]
        chat_id = update["message"]["chat"]["id"]
        #bot.sendMessage(chat_id, "From the web: you said '{}'".format(text))
        items = db.get_items(chat_id)
        if text == "/start":
            bot.sendMessage(chat_id, "Welcome to your personal To Do list. Send any text to me and I'll store it as an item. Send /done to remove items")
        elif text in items:
            db.delete_item(text, chat_id)
            items = db.get_items(chat_id)
            message = "\n".join(items)
            bot.sendMessage(chat_id, message)
            keyboard = [[item] for item in items]
            reply_markup = {"keyboard" : keyboard, "one_time_keyboard" : True}
            bot.sendMessage(chat_id, "Select an item to delete", reply_markup = json.dumps(reply_markup))
        elif text == "/done":
            bot.sendMessage(chat_id, text)
            keyboard = [[item] for item in items]
            reply_markup = {"keyboard" : keyboard, "one_time_keyboard" : True}
            bot.sendMessage(chat_id, "Select an item to delete", reply_markup = json.dumps(reply_markup))
        else:
            db.add_item(text, chat_id)
            items = db.get_items(chat_id)
            message = "\n".join(items)
            #send_message(message, chat_id)
            bot.sendMessage(chat_id, message)
    return "OK"
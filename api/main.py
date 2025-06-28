from flask import Flask, request, Response
from bot.bot import bot, process_update
import os

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.headers.get("X-Telegram-Bot-Api-Secret-Token") != os.getenv("WEBHOOK_SECRET"):
        return Response("Unauthorized", status=401)
    process_update(request.get_json())
    return Response("OK", status=200)

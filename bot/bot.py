import os
from pyrogram import Client
from bot.handlers import register_handlers

bot = Client("bot", api_id=int(os.getenv("API_ID")),
             api_hash=os.getenv("API_HASH"),
             bot_token=os.getenv("BOT_TOKEN"))

def process_update(update_json):
    bot.process_new_updates([update_json])

register_handlers(bot)

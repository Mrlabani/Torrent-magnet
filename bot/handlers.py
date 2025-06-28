from pyrogram import filters
from pyrogram.types import Message
from bot.utils import convert_magnet, log_user, error_msg
import traceback

def register_handlers(bot):
    @bot.on_message(filters.command("start"))
    async def start_handler(client, message: Message):
        await message.reply(
            "👋 Welcome to the *Magnet ➜ .torrent Bot*\n\n"
            "Send a magnet link and I’ll give you the `.torrent` file! 🔥",
            quote=True
        )
        await message.reply("🤖")
        log_user(message)

    @bot.on_message(filters.command("help"))
    async def help_handler(client, message: Message):
        await message.reply("📌 Just send a valid magnet link starting with `magnet:?xt=`")
        await message.reply("📘")

    @bot.on_message(filters.text & filters.private)
    async def magnet_handler(client, message: Message):
        text = message.text.strip()
        if text.startswith("magnet:?xt="):
            await message.reply("🧲")
            await message.chat.send_action("typing")
            try:
                log_user(message)
                torrent = await convert_magnet(text)
                if torrent:
                    await message.reply_document(torrent, caption="✅ Here’s your `.torrent` file 💾")
                    await message.reply("📦")
                else:
                    await message.reply("❌ Failed to generate `.torrent` file 😢")
                    await message.reply("❌")
            except Exception as e:
                await message.reply(error_msg(e))
                await message.reply("🚨")
        else:
            await message.reply("⚠️ Please send a valid magnet link starting with `magnet:?xt=`")
            await message.reply("😕")

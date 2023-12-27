import asyncio
from main.modules.parser import auto_parser
from main import app
from pyrogram import filters, idle
from pyrogram.types import Message
from uvloop import install
from contextlib import closing, suppress
from main.modules.tg_handler import tg_handler

loop = asyncio.get_event_loop()

@app.on_message(filters.command(["help", "ping"]))
async def start(bot, message: Message):
    await message.reply_text("⚡ **Bot Is up...**")

@app.on_message(filters.chat(-1001159872623) & filters.photo)    
async def start_bot(_, message: Message):  # Changed parameter name 'bot' to '_'
    post_id = message.message_id
    print("==================================")
    print("[INFO]: AutoAnimeBot Started Bot Successfully")
    print("==========JOIN @Latest_ongoing_airing_animes=========")
    print("[INFO]: Adding Parsing Task")
    
    # Using gather to run tasks concurrently
    await asyncio.gather(auto_parser(), tg_handler(post_id))
    
    print("[INFO]: BOT STOPPED")

if __name__ == "__main__":
    install()
    
    # Use a try-except block to handle exceptions and ensure proper cleanup
    try:
        loop.run_until_complete(idle())
    except KeyboardInterrupt:
        print("[INFO]: BOT STOPPED DUE TO KEYBOARD INTERRUPT")
    finally:
        loop.run_until_complete(app.stop())
        for task in asyncio.all_tasks():
            task.cancel()
        loop.close()

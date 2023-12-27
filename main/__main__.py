import asyncio
from main.modules.parser import auto_parser
from main import app
from pyrogram import filters, idle
from pyrogram.types import Message
from uvloop import install
from contextlib import closing, suppress
from main.modules.tg_handler import tg_handler

loop = asyncio.get_event_loop()

@app.on_message(filters.command(["help","ping"]))
async def start(bot, message: Message):
  return await message.reply_text("⚡ **Bot Is up...**")
@app.on_message(filters.chat(-1001159872623) & filters.photo)    
async def start_bot(bot, message):
  post_id = message.message_id
  print("==================================")
  print("[INFO]: AutoAnimeBot Started Bot Successfully")
  print("==========JOIN @Latest_ongoing_airing_animes=========")

  print("[INFO]: Adding Parsing Task")
  asyncio.create_task(auto_parser())
  asyncio.create_task(tg_handler(post_id))
  
  await idle()
  print("[INFO]: BOT STOPPED")
  await app.run()  


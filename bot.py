import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from config import BOT_TOKEN, ADMINS

# Log sozlamalari
logging.basicConfig(level=logging.INFO)

# Bot sozlamalari
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# Start komandasi
@dp.message_handler(commands=["start"])
async def welcome(msg: types.Message):
    await msg.answer("Assalomu alaykum!\nUmra Jet botiga xush kelibsiz.")

# Ravza bo‘limi
@dp.message_handler(lambda msg: "ravza" in msg.text.lower())
async def ravza(msg: types.Message):
    await msg.answer("🕌 *Ravza ruhsatnomasi narxi:*\n✅ Vizasi bo‘lsa: 15 SAR\n❌ Vizasi bo‘lmasa: 20 SAR\n\n24/7 ishlaymiz.", parse_mode="Markdown")

# ---------------- KEEP-ALIVE SERVER ----------------
from aiohttp import web

async def handle(request):
    return web.Response(text="UmraJet Bot is running!")

app = web.Application()
app.add_routes([web.get("/", handle)])

if __name__ == "__main__":
    import threading
    threading.Thread(target=lambda: web.run_app(app, port=10000)).start()
    executor.start_polling(dp, skip_updates=True)

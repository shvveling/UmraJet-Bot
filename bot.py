import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from config import BOT_TOKEN, ADMINS

# Log sozlamalari
logging.basicConfig(level=logging.INFO)

# Bot sozlamalari
bot = Bot(token=BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot)

# Start komandasi
@dp.message_handler(commands=["start"])
async def welcome(msg: types.Message):
    await msg.answer("👋 <b>Assalomu alaykum!</b>\nUmra Jet botiga xush kelibsiz.\nQuyidagi bo‘limlardan birini tanlang.")

# Ravza xizmati
@dp.message_handler(lambda msg: "ravza" in msg.text.lower())
async def ravza(msg: types.Message):
    await msg.answer(
        "🕌 <b>Ravza ruhsatnomasi xizmati:</b>\n\n"
        "✅ Vizasi bo‘lsa: <b>15 SAR</b>\n"
        "❌ Vizasi bo‘lmasa: <b>20 SAR</b>\n\n"
        "📆 <i>24/7 buyurtma qilish mumkin</i>\n"
        "📩 @vip_arabiy bilan bog‘laning.",
    )

# ------------------ KEEP-ALIVE WEB SERVER (Render uchun) ------------------
from aiohttp import web

async def handle(request):
    return web.Response(text="UmraJet bot is running!")

app = web.Application()
app.add_routes([web.get("/", handle)])

if __name__ == "__main__":
    import threading
    threading.Thread(target=lambda: web.run_app(app, port=10000)).start()
    executor.start_polling(dp, skip_updates=True)

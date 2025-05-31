
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from config import BOT_TOKEN, ADMIN_USERNAMES

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["\U0001F4CB Ravza Ruhsatnomasi", "\U0001F54C Umra Paketlari", "\U0001F4C5 Vizalar", "\U0001F3E8 Hotel / Hostel", "\U0001F374 Ovqat / Catering", "\U0001F682 Poyezd Chiptalari", "\U0001F4DE Admin bilan bog‘lanish"]
    keyboard.add(*buttons)
    await message.answer("Xush kelibsiz! Quyidagi xizmatlardan birini tanlang:", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == "\U0001F4CB Ravza Ruhsatnomasi")
async def ravza(message: types.Message):
    await message.answer("Ravzaga tashrif uchun ruhsatnoma xizmati.\n\n\U0001F4B0 Narxlar:\n\u2705 Vizasi bo‘lsa: 15 SAR\n\u274C Vizasi bo‘lmasa: 20 SAR\n\n\U0001F4DD Buyurtma berish uchun @vip_arabiy ga yozing.")

@dp.message_handler(lambda message: message.text == "\U0001F54C Umra Paketlari")
async def umra(message: types.Message):
    await message.answer("\U0001F54C Umra paketlari:\n\n1. Asosiy: 1200$\n2. O‘rta: 1500$\n3. VIP: 2100$\n\nBatafsil ma’lumot uchun @vip_arabiy bilan bog‘laning.")

@dp.message_handler(lambda message: message.text == "\U0001F4C5 Vizalar")
async def vizalar(message: types.Message):
    await message.answer("\U0001F4C5 Vizalar xizmati:\n\n\u2709 Umra viza: 160$\n\u2709 Turist viza: 120$\n\nKerakli hujjatlar: pasport rasmi, shaxsiy surat.")

@dp.message_handler(lambda message: message.text == "\U0001F3E8 Hotel / Hostel")
async def hotel(message: types.Message):
    await message.answer("\U0001F3E8 Hotel va Hostel xizmatlari:\n\nAsosan Makka va Madinada.\nNarxlar xona turi va odam soniga qarab belgilanadi.\n\nBuyurtma uchun: @vip_arabiy")

@dp.message_handler(lambda message: message.text == "\U0001F374 Ovqat / Catering")
async def ovqat(message: types.Message):
    await message.answer("\U0001F374 Ovqatlanish (catering) xizmati:\nGuruhlar uchun ovqatlanish va ichimliklar.\nNarxlar kelishilgan holda belgilanadi.")

@dp.message_handler(lambda message: message.text == "\U0001F682 Poyezd Chiptalari")
async def train(message: types.Message):
    await message.answer("\U0001F682 HHR Train chipta xizmati:\nYonalish va viza asosida belgilanadi.\nOddiy va VIP mavjud.")

@dp.message_handler(lambda message: message.text == "\U0001F4DE Admin bilan bog‘lanish")
async def admin(message: types.Message):
    await message.answer("\U0001F4E2 Biz bilan bog‘laning:\n\n@vip_arabiy (Asosiy manager)\n@V001VB (Yordamchi manager)")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

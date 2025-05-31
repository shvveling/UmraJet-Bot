# Umra Jet Premium Bot - Uzbek Only Version
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler

TOKEN = "YOUR_BOT_TOKEN_HERE"

services = {
    "ravza": {"viza": 15, "vizasiz": 20},
    "umra": {"viza": 160, "turist": 120},
    "train": {"oddiy": "Managerdan so‘raladi", "vip": "Managerdan so‘raladi"},
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    kb = [
        [InlineKeyboardButton("🕌 Ravza ruhsatnomasi", callback_data="ravza")],
        [InlineKeyboardButton("🕋 Umra vizasi", callback_data="umra")],
        [InlineKeyboardButton("🚄 HHR Train (Poezd)", callback_data="train")],
        [InlineKeyboardButton("📞 Admin bilan bog‘lanish", url="https://t.me/vip_arabiy")]
    ]
    await update.message.reply_text(
        "Assalomu alaykum! UmraJet xizmat botiga xush kelibsiz.",
        reply_markup=InlineKeyboardMarkup(kb)
    )

async def callback_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data
    if data in services:
        if data == "ravza":
            msg = "🕌 *Ravza Ruhsatnomasi*
Narxlar:
✅ Vizasi bo‘lsa: 15 SAR
❌ Vizasi bo‘lmasa: 20 SAR"
        elif data == "umra":
            msg = "🕋 *Umra Vizasi*
Narxlar:
✅ Umra vizasi: 160$
📌 Turist vizasi: 120$"
        elif data == "train":
            msg = "🚄 *HHR Train Xizmatlari*
- Oddiy: Managerdan so‘raladi
- VIP: Managerdan so‘raladi"
        await query.edit_message_text(msg, parse_mode="Markdown")

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(callback_handler))
    app.run_polling()

if __name__ == "__main__":
    main()

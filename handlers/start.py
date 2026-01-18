from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Bot ishga tushganda yoki /start buyrug'i berilganda ishlaydigan funksiya"""
    user = update.effective_user.first_name

    # Agar telefon raqam allaqachon saqlangan bo'lsa
    if context.user_data.get("phone"):
        keyboard = [[KeyboardButton("📅 Kelajak uchun xabar qoldirish")]]
        
        await update.message.reply_text(
            f"Qaytib kelganingizdan xursandmiz, {user}! 👋\n\n"
            f"Saqlangan raqam: {context.user_data['phone']}\n\n"
            "Davom etishingiz mumkin:",
            reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        )
        return

    # Telefon raqam so'rash
    keyboard = [
        [KeyboardButton("📞 Telefon raqamimni yuborish", request_contact=True)]
    ]

    await update.message.reply_text(
        f"Assalomu alaykum, {user}! 👋\n\n"
        "🤖 Men kelajak uchun xabar rejalashtirish botiman.\n\n"
        "📱 Siz istagan vaqtga xabar qoldirishingiz mumkin va men "
        "o'sha vaqtda sizga eslatma yuboraman.\n\n"
        "🔐 Davom etish uchun telefon raqamingizni yuboring:",
        reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True)
    )
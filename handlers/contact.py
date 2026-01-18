from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import ContextTypes

async def handle_contact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Foydalanuvchi telefon raqamini qabul qilish"""
    phone = update.message.contact.phone_number

    # Telefon raqamini saqlash
    context.user_data["phone"] = phone

    # Asosiy menyu tugmalari
    keyboard = [
        [KeyboardButton("📅 Kelajak uchun xabar qoldirish")]
    ]

    # Tasdiqlash xabari
    await update.message.reply_text(
        f"Raqam saqlandi: {phone} ✅\n\nEndi davom etamiz:",
        reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    )
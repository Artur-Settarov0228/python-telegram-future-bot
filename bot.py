from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
import logging

from config import TOKEN
from handlers.start import start
from handlers.reminder import test_reminder  # Faqat test import qiling
from handlers.contact import handle_contact

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

def main():
    if not TOKEN:
        logger.error("TOKEN topilmadi!")
        return
    
    app = ApplicationBuilder().token(TOKEN).build()

    # Faqat test komanda
    app.add_handler(CommandHandler("test", test_reminder))
    
    logger.info("🤖 Bot ishga tushmoqda...")
    logger.info("📝 /test komandasi bilan sinab ko'ring")
    
    app.run_polling(drop_pending_updates=True)

if __name__ == "__main__":
    main()
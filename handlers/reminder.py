from telegram import Update
from telegram.ext import ContextTypes
from services.scheduler import send_scheduled
import logging

logger = logging.getLogger(__name__)

async def test_reminder(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """ODDIY TEST - 10 soniya"""
    logger.info("=" * 50)
    logger.info("🧪 TEST STARTED")
    logger.info(f"Chat ID: {update.effective_chat.id}")
    logger.info("=" * 50)
    
    await update.message.reply_text(
        "🧪 TEST BOSHLANDI\n\n"
        "10 soniyadan keyin xabar kelishi kerak...\n"
        "Konsolni kuzatib turing!"
    )
    
    job = context.job_queue.run_once(
        send_scheduled,
        when=10,
        data={
            "chat_id": update.effective_chat.id,
            "text": "🎉 TEST MUVAFFAQIYATLI!\n\nScheduler ishlayapti!",
            "phone": None
        },
        name=f"test_{update.effective_chat.id}"
    )
    
    logger.info(f"✅ Test job created: {job.name}")
    logger.info("⏰ Waiting 10 seconds...")
    logger.info("=" * 50)
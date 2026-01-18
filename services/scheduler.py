from telegram.ext import ContextTypes
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

async def send_scheduled(context: ContextTypes.DEFAULT_TYPE):
    """Rejalashtirilgan xabarni yuborish"""
    logger.info("=" * 50)
    logger.info("🔔 SCHEDULED JOB TRIGGERED!")
    logger.info("=" * 50)
    
    job = context.job
    
    chat_id = job.data["chat_id"]
    text = job.data["text"]
    phone = job.data.get("phone")
    
    logger.info(f"📤 Chat ID: {chat_id}")
    logger.info(f"💬 Text: {text}")
    logger.info(f"📞 Phone: {phone}")

    try:
        result = await context.bot.send_message(
            chat_id=chat_id,
            text=f"⏰ Rejalashtirilgan xabar:\n\n{text}\n\n"
                 f"📅 Vaqt: {datetime.now().strftime('%Y-%m-%d %H:%M')}"
        )
        
        logger.info(f"✅ MESSAGE SENT SUCCESSFULLY! Message ID: {result.message_id}")
        logger.info("=" * 50)

    except Exception as e:
        logger.error(f"❌ ERROR SENDING MESSAGE: {e}")
        logger.error("=" * 50)
        
        try:
            await context.bot.send_message(
                chat_id=chat_id,
                text=f"❌ Xatolik: {str(e)}"
            )
        except:
            logger.error("Failed to send error message too!")
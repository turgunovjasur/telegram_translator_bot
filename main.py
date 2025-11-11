"""
Telegram Translator Bot - Asosiy fayl
"""
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackQueryHandler
from config import settings
from handlers import (
    start_command,
    change_language_command,
    button_callback_handler,
    translate_message_handler
)


def main():
    """Botni ishga tushirish"""
    
    # Settings validatsiyasi
    try:
        settings.validate()
    except ValueError as e:
        print(f"❌ Xatolik: {e}")
        print("💡 .env faylni tekshiring!")
        return
    
    # Application yaratish
    app = Application.builder().token(settings.TELEGRAM_BOT_TOKEN).build()
    
    # Handlerlar qo'shamiz
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("change", change_language_command))
    app.add_handler(CallbackQueryHandler(button_callback_handler))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, translate_message_handler))
    
    print("🤖 Bot ishga tushdi! Telegram'da /start bosing.")
    print("⛔ To'xtatish uchun: Ctrl+C")
    
    # Botni ishga tushirish
    app.run_polling()


if __name__ == '__main__':
    main()

"""
Bot konfiguratsiyasi va sozlamalari
"""
import os
from dotenv import load_dotenv

# .env faylni yuklash
load_dotenv()


class Settings:
    """Bot sozlamalari"""
    
    # API kalitlar
    GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
    TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
    
    # Gemini model nomi
    GEMINI_MODEL = 'gemini-2.0-flash'
    
    # Rate limit sozlamalari
    RATE_LIMIT_WAIT_TIME = 60  # sekund
    MAX_REQUESTS_PER_MINUTE = 15

    # Matn limitlari - YANGI
    MAX_INPUT_LENGTH = 1000  # Input uchun limit (belgi)
    MAX_TELEGRAM_MESSAGE_LENGTH = 4096  # Telegram limiti
    
    def validate(self):
        """API kalitlarni tekshirish"""
        if not self.GEMINI_API_KEY:
            raise ValueError("GEMINI_API_KEY topilmadi!")
        if not self.TELEGRAM_BOT_TOKEN:
            raise ValueError("TELEGRAM_BOT_TOKEN topilmadi!")


# Settings instansiyasi
settings = Settings()

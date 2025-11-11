"""
Bot xabarlari va matnlari
"""


class Messages:
    """Bot xabarlari"""
    
    # Start xabari
    START_MESSAGE = (
        "👋 Assalomu alaykum!\n\n"
        "Men tarjimon botman. Qaysi yo'nalishda tarjima qilishimni tanlang:"
    )
    
    # Til sozlamalari
    UZ_TO_ENG_SET = "✅ Sozlandi: 🇺🇿 O'zbek → 🇬🇧 Ingliz\n\nEndi o'zbek tilidagi matn yuboring!"
    ENG_TO_UZ_SET = "✅ Sozlandi: 🇬🇧 Ingliz → 🇺🇿 O'zbek\n\nEndi ingliz tilidagi matn yuboring!"
    
    # Change xabari
    CHANGE_MESSAGE = "🔄 Yangi yo'nalishni tanlang:"
    
    # Xatolik xabarlari
    NO_LANGUAGE_SELECTED = (
        "⚠️ Iltimos, avval til yo'nalishini tanlang!\n\n"
        "/start buyrug'ini bosing."
    )
    
    TRANSLATING = "⏳ Tarjima qilyapman..."
    
    RATE_LIMIT_ERROR = (
        "⚠️ Siz juda ko'p xabar yubordingiz!\n\n"
        "⏰ Iltimos, birozdan keyin qayta urinib ko'ring.\n\n"
        "💡 Maslahat: Bepul versiyasida daqiqada 15 ta so'rov limiti bor."
    )
    
    GENERAL_ERROR = (
        "❌ Xatolik yuz berdi.\n\n"
        "Iltimos, qaytadan urinib ko'ring!"
    )
    
    # Tugmalar matni
    BUTTON_UZ_TO_ENG = "🇺🇿 → 🇬🇧 O'zbek → Ingliz"
    BUTTON_ENG_TO_UZ = "🇬🇧 → 🇺🇿 Ingliz → O'zbek"
    
    @staticmethod
    def format_translation_result(original_text: str, translated_text: str, direction: str) -> str:
        """Tarjima natijasini formatlash"""
        if direction == 'uz_to_eng':
            return f"🇺🇿 O'zbekcha:\n{original_text}\n\n🇬🇧 Inglizcha:\n{translated_text}"
        else:
            return f"🇬🇧 Inglizcha:\n{original_text}\n\n🇺🇿 O'zbekcha:\n{translated_text}"

    # Uzun matn xabari - YANGI
    @staticmethod
    def text_too_long_error(text_length: int, max_length: int) -> str:
        return (
            f"⚠️ Matn juda uzun!\n\n"
            f"📊 Sizning matn: {text_length} belgi\n"
            f"📊 Maksimal: {max_length} belgi\n\n"
            f"💡 Iltimos, qisqaroq matn yuboring."
        )

# Messages instansiyasi
messages = Messages()

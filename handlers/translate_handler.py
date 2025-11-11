"""
Matnni tarjima qilish uchun handler
"""
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.error import BadRequest
from telegram.ext import ContextTypes
from services import translator_service
from utils import messages
from .button_handler import get_user_language


def _create_keyboard():
    """Til o'zgartirish tugmalarini yaratish"""
    keyboard = [
        [InlineKeyboardButton(messages.BUTTON_UZ_TO_ENG, callback_data='uz_to_eng')],
        [InlineKeyboardButton(messages.BUTTON_ENG_TO_UZ, callback_data='eng_to_uz')]
    ]
    return InlineKeyboardMarkup(keyboard)


# _create_keyboard funksiyadan keyin quyidagini qo'shing:
MAX_TELEGRAM_MESSAGE_LENGTH = 4096
MAX_INPUT_LENGTH = 1000  # Input uchun limit

async def translate_message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Foydalanuvchi yuborgan matnni tarjima qiladi"""
    user_id = update.effective_user.id
    user_text = update.message.text

    # Matn uzunligini tekshirish - YANGI
    if len(user_text) > MAX_INPUT_LENGTH:
        await update.message.reply_text(
            f"⚠️ Matn juda uzun!\n\n"
            f"📊 Sizning matn: {len(user_text)} belgi\n"
            f"📊 Maksimal: {MAX_INPUT_LENGTH} belgi\n\n"
            f"💡 Iltimos, qisqaroq matn yuboring.",
            reply_markup=_create_keyboard()
        )
        return

    # Agar user til tanlamagan bo'lsa
    direction = get_user_language(user_id)
    if not direction:
        await update.message.reply_text(
            messages.NO_LANGUAGE_SELECTED,
            reply_markup=_create_keyboard()
        )
        return
    
    # Kutish xabarini yuborish
    waiting_msg = await update.message.reply_text(messages.TRANSLATING)
    
    try:
        # Tarjima qilish
        translated_text = await translator_service.translate(user_text, direction)

        # Javobni formatlash
        result = messages.format_translation_result(user_text, translated_text, direction)

        # Natija uzunligini tekshirish - YANGI
        if len(result) > MAX_TELEGRAM_MESSAGE_LENGTH:
            # Agar juda uzun bo'lsa, qisqartirish
            max_text_length = (MAX_TELEGRAM_MESSAGE_LENGTH - 200) // 2  # 200 - formatlar uchun

            truncated_original = user_text[:max_text_length] + "..."
            truncated_translation = translated_text[:max_text_length] + "..."

            result = messages.format_translation_result(
                truncated_original,
                truncated_translation,
                direction
            )
            result += "\n\n⚠️ Matn juda uzun bo'lgani uchun qisqartirildi."

        # Kutish xabarini o'chirish - YANGI (xatolikni boshqarish)
        try:
            await waiting_msg.delete()
        except BadRequest:
            pass  # Agar xabar allaqachon o'chirilgan bo'lsa, o'tkazib yuboramiz
        
        # Javobni formatlash va yuborish (tugmalar bilan)
        result = messages.format_translation_result(user_text, translated_text, direction)

        await update.message.reply_text( result, reply_markup=_create_keyboard())
        
    except Exception as e:
        error_text = str(e)
        
        # Kutish xabarini o'chirish - YANGI (xatolikni boshqarish)
        try:
            await waiting_msg.delete()
        except BadRequest:
            pass  # Agar xabar allaqachon o'chirilgan bo'lsa, o'tkazib yuboramiz
        
        # Rate Limit xatosini aniqlash
        if "429" in error_text or "quota" in error_text.lower() or "rate limit" in error_text.lower():
            await update.message.reply_text(
                messages.RATE_LIMIT_ERROR,
                reply_markup=_create_keyboard()
            )
        else:
            await update.message.reply_text(
                messages.GENERAL_ERROR,
                reply_markup=_create_keyboard()
            )
        
        print(f"❌ Xatolik: {error_text}")

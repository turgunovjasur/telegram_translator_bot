"""
Inline tugmalar uchun handler
"""
from telegram import Update
from telegram.ext import ContextTypes
from utils import messages

# Userlarning til sozlamalarini saqlash uchun dictionary
# {user_id: 'uz_to_eng' yoki 'eng_to_uz'}
user_languages = {}


async def button_callback_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Inline tugma bosilganda til sozlamalarini saqlaydi"""
    query = update.callback_query
    await query.answer()  # Tugma bosilganini tasdiqlash
    
    user_id = query.from_user.id
    choice = query.data  # 'uz_to_eng' yoki 'eng_to_uz'
    
    # Userni xotirada saqlash
    user_languages[user_id] = choice
    
    # Tasdiqlash xabari
    if choice == 'uz_to_eng':
        message = messages.UZ_TO_ENG_SET
    else:
        message = messages.ENG_TO_UZ_SET
    
    # Eski xabarni o'chirmasdan yangi xabar yuborish
    await query.message.reply_text(message)
    
    # Tugma bosilganini ko'rsatish uchun
    await query.answer("✅ Til o'zgartirildi!")


def get_user_language(user_id: int) -> str | None:
    """
    Foydalanuvchi tanlagan til yo'nalishini olish
    
    Args:
        user_id: Telegram user ID
        
    Returns:
        'uz_to_eng', 'eng_to_uz' yoki None
    """
    return user_languages.get(user_id)

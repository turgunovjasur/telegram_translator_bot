"""
/start buyrug'i uchun handler
"""
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from utils import messages


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Bot ishga tushganda til tanlash tugmalarini ko'rsatadi"""
    
    # Tugmalar yaratamiz
    keyboard = [
        [InlineKeyboardButton(messages.BUTTON_UZ_TO_ENG, callback_data='uz_to_eng')],
        [InlineKeyboardButton(messages.BUTTON_ENG_TO_UZ, callback_data='eng_to_uz')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(messages.START_MESSAGE, reply_markup=reply_markup)


async def change_language_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Til sozlamalarini o'zgartirish"""
    keyboard = [
        [InlineKeyboardButton(messages.BUTTON_UZ_TO_ENG, callback_data='uz_to_eng')],
        [InlineKeyboardButton(messages.BUTTON_ENG_TO_UZ, callback_data='eng_to_uz')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(messages.CHANGE_MESSAGE, reply_markup=reply_markup)

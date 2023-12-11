from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


tasdiqlash = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="OK", callback_data='ok'), InlineKeyboardButton(text="NO", callback_data="no")]
    ]
)



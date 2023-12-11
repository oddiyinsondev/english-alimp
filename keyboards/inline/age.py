from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


ages = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="4-sinf", callback_data='4-sinf'), InlineKeyboardButton(text="6-sinf", callback_data="6-sinf")],
        [InlineKeyboardButton(text="5-sinf", callback_data='5-sinf'), InlineKeyboardButton(text="7-sinf", callback_data="7-sinf")],
    ]
)



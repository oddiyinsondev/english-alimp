from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


start_button = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="⭐️ Start Registration")],
        [KeyboardButton(text="About US"), KeyboardButton(text="Settings")],
    ],
    resize_keyboard=True,
    
)


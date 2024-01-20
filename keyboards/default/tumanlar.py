from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


tumanlar = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Bog'ot tumani"), KeyboardButton(text="Gurlan tumani")],
        [KeyboardButton(text="Qo'shko'pir tumani"), KeyboardButton(text="Shovot tumani")],
        [KeyboardButton(text="Urganch shahri"), KeyboardButton(text="Urganch tumani")],
        [KeyboardButton(text="Xazorasp tumani"), KeyboardButton(text="Xiva tumani")],
        [KeyboardButton(text="Xonqa tumani"), KeyboardButton(text="Yangiariq tumani")],
        [KeyboardButton(text="Yangibozor tumani"), KeyboardButton(text="Tuproq qa'la tumani")]
    ]
)
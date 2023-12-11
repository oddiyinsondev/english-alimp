
from typing import Union
from aiogram import Bot


async def chek(user_id, channel: Union[int, str]):
    bot = Bot.get_current()
    member = await bot.get_chat_member(user_id=user_id, chat_id=channel)
    return member.is_chat_member()
    

# bu funksiya ishlashi uchun siz botni kannalga qo'shib adminlik berish kerak

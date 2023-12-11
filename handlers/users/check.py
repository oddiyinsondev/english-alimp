from loader import dp, bot
from data.config import CHANNELS
from utils.misc import subscription
from aiogram import types
from keyboards.default.start_button import start_button
from keyboards.inline.obuna import check_button


@dp.callback_query_handler(text="check_subs")
async def checker(call: types.CallbackQuery):
    await call.answer("Obuna tekshirildi")
    final_status = True
    result = str()
    for channel in CHANNELS:
        status = await subscription.chek(user_id=call.from_user.id,
                                          channel=channel)
        channel = await bot.get_chat(channel)
        if status:
            final_status *= status
            result += f"✅ <b>{channel.title}</b> kanaliga obuna bo'lgansiz!\n\n"
        
        else:
            final_status *= False
            invite_link = await channel.export_invite_link()
            result += (f"❌ <a href='{invite_link}'><b>{channel.title}</b></a> kanaliga obuna bo'lmagansiz.\n\n")
    
    if final_status:
        await call.message.delete()
        msg = f"Assalomu alaykum xush kelibsiz\n👤 <b>{call.from_user.full_name}</b>!\nRegistratsiyani boshlaymizmi 🔽" 
        await call.message.answer(msg, reply_markup=start_button)
    else:
        await call.message.delete()
        await call.message.answer(result, disable_web_page_preview=True, reply_markup=check_button)
from loader import dp
from aiogram import types
from keyboards.inline.age import ages
from states.sinf6 import sinf6
from keyboards.inline.tasdiqlash import tasdiqlash
from aiogram.dispatcher.filters import state
from aiogram.dispatcher import FSMContext
from keyboards.default.tumanlar import tumanlar
kanal_data = "-1001632556657"



def fayl_7(t_ism):
    with open("sinf7",'w') as fayl:
        fayl.write(t_ism + "\n")



@dp.callback_query_handler(text="7-sinf")
async def senism(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"Toliq ism familyangizni kiriting: ")
    await sinf6.fish.set()


@dp.message_handler(state=sinf6.fish)
async def fish(message: types.Message, state: FSMContext):
    FISH = message.text
    await state.update_data(
        {"FISH":FISH}
    )
    await message.answer("maktabingiz haqida malumot bering misol uchun\n 2-son maktab")
    await sinf6.next()



@dp.message_handler(state=sinf6.maktab)
async def tuman(message: types.Message, state: FSMContext):
    maktab = message.text
    await state.update_data(
        {"maktab": maktab}
    )
    await message.answer("uqtuvchingiz ismini kiriting:")
    await sinf6.next()


@dp.message_handler(state=sinf6.uqtuvchi)
async def tuman(message: types.Message, state: FSMContext):
    uqtuvchi = message.text
    await state.update_data(
        {"uqtuvchi": uqtuvchi}
    )
    await message.answer("Uqtuvchingizni telefon nomr yuboring")
    await sinf6.next()



@dp.message_handler(state=sinf6.tel_nomr)
async def tuman(message: types.Message, state: FSMContext):
    phone_number = message.text
    await state.update_data(
        {"phone_number": phone_number}
    )
    await message.answer("Iltimos tumaningizni tanlang: ", reply_markup=tumanlar)
    await sinf6.next()


@dp.message_handler(state=sinf6.tuman)
async def tuman(message: types.Message, state: FSMContext):
    tuman = message.text
    await state.update_data(
        {"tuman": tuman}
    )
    await message.answer_photo(photo=open("img/card.gif", "rb"), caption="tolovni qilib skrinshot yuboring: ")
    await sinf6.next()



@dp.message_handler(state=sinf6.tolov, content_types=["photo"])
async def tuman(message: types.Message, state: FSMContext):
    photo = message.photo[-1].file_id
    await state.update_data(
        {"photo": photo}
    )
    data = await state.get_data()
    fish = data.get("FISH")
    maktab = data.get("maktab")
    uqtuvchi = data.get("uqtuvchi")
    phone_number = data.get("phone_number")
    tuman = data.get("tuman")
    photo1 = data.get("photo")
    await message.answer_photo(photo=photo1, caption=f"Tumaningiz: {tuman}\nMaktabingiz: {maktab}\nUqtuvchingiz: {uqtuvchi}\nUqtuvchingiz telefoni: {phone_number}\nSizning FISH: {fish}", reply_markup=tasdiqlash)
    await sinf6.next()



@dp.callback_query_handler(state=sinf6.admin, text='no')
async def admin_send(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.message.delete()
    await callback_query.message.answer_photo(photo=open("img/english.jpg", "rb"), caption="Sinfingizni kiriting? ", reply_markup=ages) 
    await state.finish()





@dp.callback_query_handler(state=sinf6.admin, text='ok')
async def admin_send(callback_query: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    fish = data.get("FISH")
    maktab = data.get("maktab")
    uqtuvchi = data.get("uqtuvchi")
    phone_number = data.get("phone_number")
    tuman = data.get("tuman")
    photo1 = data.get("photo")
    await callback_query.message.edit_reply_markup()
    await callback_query.bot.send_photo(kanal_data, photo=photo1, caption=f"7-sinf \n\nTumaningiz: {tuman}\nMaktabingiz: {maktab}\nUqtuvchingiz: {uqtuvchi}\nUqtuvchingiz telefoni: {phone_number}\nSizning FISH: {fish}")
    # await callback_query.message.answer_photo(kanal_data, photo=photo1, caption=f"Tumaningiz: {tuman}\nMaktabingiz: {maktab}\nUqtuvchingiz: {uqtuvchi}\nUqtuvchingiz telefoni: {phone_number}\nSizning FISH: {fish}")
    await callback_query.message.answer("Movfaqiyatli ro'yhatdan o'tdingiz!")
    t_ism = f"{tuman}  {maktab}  {uqtuvchi}  {phone_number}  {fish}  + "
    fayl_7(t_ism=t_ism)
    await state.finish()

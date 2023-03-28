import re
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher import FSMContext
from loader import dp, db, bot
from data.config import ADMINS
from keyboards.default.main import main_markup
from states.teamwork import AllStates

@dp.message_handler(text='Ro’yxatdan o’tish', state=AllStates.start)
async def get_user_degree(message: types.Message, state: FSMContext):
    await message.answer(text='Hozirda kim sifatida ro’yxatdan o’tmoqchimisiz? Tizimga kirish orqali ikkinchi rolni ham qo’shsangiz bo’ladi.')
    await AllStates.degree.set()

@dp.message_handler(text='Ish beruvchi sifatida', state=AllStates.degree)
async def get_user_phone_number(message: types.Message, state: FSMContext):
    await message.answer(text='Telefon raqamingiz (ushbu raqamga tasdiqlash kodi keladi)\n\n<i>Telefon raqamni <b>+998XXXXXXXXX</b> formatda kiriting!</i>')
    await AllStates.phone_number.set()

@dp.message_handler(state=AllStates.phone_number)
async def get_user_password1(message: types.Message, state: FSMContext):
    if re.match('/^[+]998([378]{2}|(9[013-57-9]))\d{7}$/', message.text):
        employers = await db.select_employers()
        for employer in employers:
            if employer[1] == message.text:
                await message.answer(text=f'{message.text} raqami oldin ro’yxatdan o’tgan! Boshqa raqam bilan urinib ko’ring.')
        else:
            
            await state.update_data({'phone_number': message.text})
            await message.answer(text='Parolingiz:')
            await AllStates.password1.set()
    else:
        await message.answer(text='Iltimos, telefon raqamni <b>+998XXXXXXXXX</b> formatda kiriting!')

@dp.message_handler(state=AllStates.password1)
async def get_user_password2(message: types.Message, state: FSMContext):
    await state.update_data({'password1': message.text})
    await message.answer(text='Parolni takrorlang:')
    await AllStates.password2.set()

@dp.message_handler(state=AllStates.password2)
async def check_user_code(message: types.Message, state: FSMContext):
    data = await state.get_data()
    password1 = data.get("password1")
    if password1 == message.text:
        await message.answer(text='Sizga yuborilgan tasdiqlash kodini kiriting')
        await AllStates.check_code.set()
    else:
        await message.answer(text='Parollar bir xil emas!')
        await AllStates.password1.set()

@dp.message_handler(state=AllStates.check_code)
async def get_user_degree(message: types.Message, state: FSMContext):
    pass
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp, db, bot
from data.config import ADMINS
from keyboards.default.main import main_markup
from states.teamwork import AllStates

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    name = message.from_user.username
    user = await db.select_user(telegram_id=message.from_user.id)
    if user is None:
        user = await db.add_user(
            telegram_id=message.from_user.id,
            full_name=message.from_user.full_name,
            username=message.from_user.username,
        )
        # ADMINGA xabar beramiz
        count = await db.count_users()
        msg = f"@{user[2]} bazaga qo'shildi.\nBazada {count} ta foydalanuvchi bor."
        await bot.send_message(chat_id=ADMINS[0], text=msg)
    # user = await db.select_user(telegram_id=message.from_user.id)
    await bot.send_message(chat_id=ADMINS[0], text=f"@{name} bazaga oldin qo'shilgan")
    await message.answer(f"Assalomu aleykum. Xush kelibsiz!\n\n<i>Yangi foydalanuvchi bo’lsangiz ro’yxatdan o’tish tugmasini bosing, agar avvalroq ro’yxatdan o’tgan bo’lsangiz kirish tugmasini bosing</i>", reply_markup=main_markup)
    await AllStates.start.set()

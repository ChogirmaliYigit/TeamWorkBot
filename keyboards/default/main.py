from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


main_markup = ReplyKeyboardMarkup(resize_keyboard=True)
main_markup.row(KeyboardButton(text='Kirish'))
main_markup.row(KeyboardButton(text='Ro’yxatdan o’tish'))
main_markup.row(KeyboardButton(text='Parolni tiklash'))


register_markup = ReplyKeyboardMarkup(resize_keyboard=True)
register_markup.row(KeyboardButton(text='Ish beruvchi sifatida'))
register_markup.row(KeyboardButton(text='Mutaxassis sifatida'))

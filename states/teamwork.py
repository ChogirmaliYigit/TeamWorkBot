from aiogram.dispatcher.filters.state import State, StatesGroup


class AllStates(StatesGroup):
    start = State()
    degree = State()
    phone_number = State()
    password1 = State()
    password2 = State()
    check_code = State()
    
from aiogram.fsm.state import State,StatesGroup

class Registor(StatesGroup):
    name = State()
    phone = State()
    email = State()
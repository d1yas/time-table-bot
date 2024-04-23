from aiogram.dispatcher.filters.state import State, StatesGroup


class CallbackStates(StatesGroup):
    start_state = State()
    teacher_state = State()
    student_state = State()
    zvonok_state = State()

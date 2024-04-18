from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

keyboard_def = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Расписание")
        ],
        [
            KeyboardButton(text='Время звонков')
        ],
        [
            KeyboardButton(text='О боте')
        ],
    ], resize_keyboard=True
)
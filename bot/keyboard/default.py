from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

keyboard_def = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Время звонков')
        ],
        [
            KeyboardButton(text='О боте')
        ],
        [
            KeyboardButton(text='Тех поддержка')
        ],
    ], resize_keyboard=True
)
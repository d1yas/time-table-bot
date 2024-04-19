from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto
import logging
from aiogram.types import ReplyKeyboardRemove
from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from keyboard.inline import start_menu, table_student, teacher
from keyboard.default import keyboard_def
from states import CallbackStates
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto
import sqlite3

connect = sqlite3.connect('../db.sqlite3', check_same_thread=False)
cursor = connect.cursor()

# Инициализация бота и диспетчера
API_TOKEN = '7035105679:AAHcWXjb97wm2DyH8le5juzsHNT2G9hGHu4'
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    # Создание инлайн клавиатуры для выбора роли пользователя
    markup = InlineKeyboardMarkup()
    markup.row(
        InlineKeyboardButton("Ученик", callback_data="student"),
        InlineKeyboardButton("Учитель", callback_data="teacher")
    )
    await message.reply("Кто вы?", reply_markup=markup)


@dp.callback_query_handler(lambda c: c.data == 'student' or c.data == 'teacher')
async def process_callback_button(callback_query: types.CallbackQuery):
    # Если пользователь выбрал "Ученик"
    if callback_query.data == 'student':
        # Создание инлайн клавиатуры с выбором класса
        markup = InlineKeyboardMarkup()
        for grade in range(1, 12):
            markup.row(
                InlineKeyboardButton(f"{grade} класс", callback_data=f"grade_{grade}")
            )
        markup.row(
            InlineKeyboardButton("Назад", callback_data="start")
        )
        await bot.send_message(callback_query.from_user.id, "Выберите класс:", reply_markup=markup)
    # Если пользователь выбрал "Учитель"
    elif callback_query.data == 'teacher':
        await bot.send_message(callback_query.from_user.id, "Введите имя, фамилию и отчество учителя через пробел")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

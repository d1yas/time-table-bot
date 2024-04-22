from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto
import logging
from aiogram.types import ReplyKeyboardRemove
from aiogram import Bot, Dispatcher, types, executor
from keyboard.inline_testn2 import teacher_chapter1 , teacher_chapter2
from aiogram.contrib.fsm_storage.memory import MemoryStorage
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
    await message.answer("Добро пожаловать .\nРасписание Для Учителей /teacher\nРасписание Для Учеников /student")

@dp.message_handler(commands=['teacher'])
async def teacher_command(message: types.Message):
    await message.answer("Как вас зовут\nПервый список:", reply_markup=teacher_chapter1)
    await message.answer("Второй список:",reply_markup=teacher_chapter2)
    # await message.answer("Третий список список:",reply_markup=)
    # await message.answer("Четвертый список:",reply_markup=)
    # await message.answer("Пятый список:", reply_markup=)
@dp.callback_query_handler(text='Нигора,Абдукадирова,Абдуфаттаховна')
async def teach1(call: types.CallbackQuery):








if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

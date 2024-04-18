import logging
from aiogram.types import ReplyKeyboardRemove
from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from keyboard.inline import start_menu, table_student,  teacher
from keyboard.default import keyboard_def
from states import CallbackStates
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto

# ------------------------DATABASE--------------------
from aiogram.dispatcher import FSMContext
import sqlite3
from aiogram.types import InputMedia

connect = sqlite3.connect('../db.sqlite3', check_same_thread=False)
cursor = connect.cursor()
# from environs import Env


# env = Env()
# env.read_env()
#


# API_TOKEN = env.str("API_TOKEN")
# ADMINS = env.list("ADMINS")
# IP = env.str("ip")

# ------------------------DATABASE--------------------
API_TOKEN = '7035105679:AAHcWXjb97wm2DyH8le5juzsHNT2G9hGHu4'




logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot, storage=MemoryStorage())



# @dp.message_handler(commands=['search'])
# async def search(message: types.Message):
#     def find_teacher(name, surname, patronymic):
#         cursor.execute("SELECT * FROM UserApp_teachermodel WHERE name = ? AND surname = ? AND patronymic = ?",
#                        (name, surname, patronymic))
#         return cursor.fetchall()
#     user_input = message.text.split()
#     if len(user_input) != 4:
#         await message.reply("Неправильный формат запроса. Используйте: /search <name> <surname> <patronymic>")
#         return
#     _, name, surname, patronymic = user_input
#     teachers = find_teacher(name, surname, patronymic)
#     if teachers:
#         for teacher in teachers:
#             teacher_info = f"Имя: {teacher[1]}\nФамилия: {teacher[2]}\nОтчество: {teacher[3]}"
#             await message.reply(teacher_info)
#     else:
#         await message.reply("Учитель не найден")
#
#
#
# @dp.message_handler(commands='start')
# async def start_bot(message: types.Message):
#     await message.answer("Добро пожаловать . ", reply_markup=keyboard_def)
#     await CallbackStates.start_state.set()
#
# @dp.message_handler(text="Расписание")
# async def ros(message: types.Message):
#     await message.answer("Выберите Категорию", reply_markup=start_menu)
# @dp.callback_query_handler(text="Для учеников")
# async def student_btn(call: types.CallbackQuery):
#
#
#
#
# # @dp.message_handler(text="Я ученик")
# # async def student(message: types.Message):
# #     await message.answer("Выберите класс")
# #     await message.answer('Class', reply_markup=table_student)
#
#
#
# @dp.message_handler(text="Время звонков")
# async def time_zv(message: types.Message):
#     await message.answer("Время звоноков")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
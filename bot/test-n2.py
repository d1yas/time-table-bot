from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher import FSMContext
import logging
from aiogram.types import ReplyKeyboardRemove
from aiogram import Bot, Dispatcher, types, executor
from keyboard.inline_testn2 import teacher
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
async def process_start_command(message: types.Message, state: FSMContext):
    await message.answer("Добро пожаловать .\nРасписание Для Учителей /teacher\nРасписание Для Учеников /student",
                         reply_markup=keyboard_def)
    await CallbackStates.start_state.set()
    await state.finish()


@dp.message_handler(text="О боте")
async def about_bot(message: types.Message):
    await message.answer("Этот бот зделан дял школы 210 .\nЧто бы видеть расписание учеников и учетилей")


@dp.message_handler(commands=['teacher'])
async def teacher_command(message: types.Message):
    await message.answer("Как вас зовут", reply_markup=teacher)
    await CallbackStates.teacher_state.set()


@dp.callback_query_handler(text="Джураева С. А.")
async def teach1(call: types.CallbackQuery, state: FSMContext):
    if call.data != "dsa":
        teacher_info = call.data
        print(teacher_info)
        global a
        a = cursor.execute("SELECT * FROM UserApp_teachermodel WHERE name=?", (teacher_info,)).fetchall()
        # teacher_fio = cursor.execute(f"SELECT name FROM UserApp_teachermodel WHERE id = {teacher_images[0][-2]}").fetchone()
        message_img = f'''
ФИО Учителя {a[0][1]}
'''
        media_group = [
            InputMediaPhoto(media=open(
                f'../{a[0][2]}', 'rb'), caption=message_img)
        ]
        print(a)
        print(teacher_info)
        await call.message.answer_media_group(media=media_group)
        await state.finish()

# @dp.callback_query_handler()
# async def teach1(call: types.CallbackQuery, state: FSMContext):
#     teacher_info = call.data
#     print(teacher_info)
#     global a
#     a = cursor.execute("SELECT * FROM UserApp_teachermodel WHERE name=?", (teacher_info,)).fetchall()
#     # teacher_fio = cursor.execute(f"SELECT name FROM UserApp_teachermodel WHERE id = {teacher_images[0][-2]}").fetchone()
#     message_img = f'''
# ФИО Учителя {a[0][1]}
# '''
#     media_group = [
#         InputMediaPhoto(media=open(
#             f'../{a[0][2]}', 'rb'), caption=message_img)
#     ]
#     print(teacher_info)
#     await call.message.answer_media_group(media=media_group)
#     await state.finish()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

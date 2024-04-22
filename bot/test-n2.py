from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto
import logging
from aiogram.types import ReplyKeyboardRemove
from aiogram import Bot, Dispatcher, types, executor
from keyboard.inline_testn2 import teacher
from keyboard.default import keyboard_def
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from keyboard.default import keyboard_def
from states import CallbackStates
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto
import sqlite3
# from UserApp.models import TeacherModel, StudentModel

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
    await message.answer("Добро пожаловать .\nРасписание Для Учителей /teacher\nРасписание Для Учеников /student", reply_markup=keyboard_def)

@dp.message_handler(text="О боте")
async def about_bot(message: types.Message):
    await message.answer("Этот бот зделан дял школы 210 .\nЧто бы видеть расписание учеников и учетилей")

@dp.message_handler(commands=['teacher'])
async def teacher_command(message: types.Message):
    await message.answer("Как вас зовут", reply_markup=teacher)


# @dp.callback_query_handler()
# async def teach1(call: types.CallbackQuery):
#     if call.data != "dsa":
#         teacher_info = call.data
#         print(call.data)
#         print(teacher_info)
#         global a
#         a = cursor.execute(
#             f"SELECT * FROM UserApp_teachermodel WHERE name=?", (teacher_info)).fetchall()
#         # teacher_fio = cursor.execute(f"SELECT name FROM UserApp_teachermodel WHERE id = {teacher_images[0][-2]}").fetchone()
#         message_img = f'''
# ФИО Учителя {teacher_info[0][1]}
# '''
#         media_group = [
#             InputMediaPhoto(media=open(
#                 f'../{a[0][2]}', 'rb'), caption=message_img)
#         ]
#
#         await call.message.answer_media_group(media=media_group)
@dp.callback_query_handler()
async def teach1(call: types.CallbackQuery):
    print(False)
    if call.data == "dsa":
        teacher_info = call.data
        print(True)
        print(call.data)
        print(teacher_info)
        # Используйте метод objects.filter() для получения данных из базы данных
        teachers = TeacherModel.objects.filter(name=teacher_info)
        if teachers.exists():  # Проверьте, есть ли какие-либо результаты
            teacher = teachers.first()  # Получите первого учителя из результата запроса
            message_img = f'''
ФИО Учителя {teacher.name}
'''
            media_group = [
                InputMediaPhoto(media=open(
                    f'{teacher.image_path}', 'rb'), caption=message_img)  # Предполагается, что в вашей модели есть поле image_path, содержащее путь к изображению
            ]
            await call.message.answer_media_group(media=media_group)
        else:
            await call.message.answer("Нет данных об учителе.")






if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

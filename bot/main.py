import logging
from aiogram.types import ReplyKeyboardRemove
from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from keyboard.inline import start_menu, table_student ,  teacher
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
API_TOKEN = '7035105679:AAHcWXjb97wm2DyH8le5juzsHNT2G9hGHu4'

# API_TOKEN = env.str("API_TOKEN")
# ADMINS = env.list("ADMINS")
# IP = env.str("ip")

# ------------------------DATABASE--------------------

def find_teacher(name, surname, patronymic):
    cursor.execute("SELECT * FROM UserApp_teachermodel WHERE name = ? AND surname = ? AND patronymic = ?", (name, surname, patronymic))
    return cursor.fetchall()



logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands=['search'])
async def search(message: types.Message):
    user_input = message.text.split()
    if len(user_input) != 4:
        await message.reply("Неправильный формат запроса. Используйте: /search <name> <surname> <patronymic>")
        return
    _, name, surname, patronymic = user_input
    teachers = find_teacher(name, surname, patronymic)
    if teachers:
        for teacher in teachers:
            teacher_info = f"Имя: {teacher[1]}\nФамилия: {teacher[2]}\nОтчество: {teacher[3]}"
            await message.reply(teacher_info)
    else:
        await message.reply("Учитель не найден")



@dp.message_handler(commands='start')
async def start_bot(message: types.Message):
    await message.answer("Добро пожаловать .\nКем вы являетесь ? ", reply_markup=start_menu)

@dp.message_handler(text="Я ученик")
async def student(message: types.Message):
    await message.answer("Выберите класс")
    await message.answer('Class', reply_markup=table_student)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
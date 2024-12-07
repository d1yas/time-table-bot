import logging
import sqlite3
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from keyboards.default import keyboard_def
from config import ADMIN_ID, TOKEN


UPLOADS = "C:/Users/steam/PycharmProjects/time-table-bot/"
connect = sqlite3.connect("C:/Users/steam/PycharmProjects/time-table-bot/db.sqlite3", check_same_thread=False)
cursor = connect.cursor()

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


async def send_message_to_admin(user: types.User, message_text: str):
    await bot.send_message(ADMIN_ID, f"Этот пользователь @{user.username} ({user.id}) написал: \"{message_text}\"")


# state
class Shogirdchala(StatesGroup):
    list_class = State()
    class_data = State()
    teacher_data = State()
    zvanok = State()


# Handlers
@dp.message_handler(commands='start')
async def process_start_command(message: types.Message):
    user = message.from_user
    message_text = message.text
    await send_message_to_admin(user, message_text)
    await message.answer("Добро Пожаловать", reply_markup=keyboard_def)




@dp.message_handler(text="Расписание классов🧑‍🎓")
async def class_schedule(message: types.Message, state: FSMContext):
    user = message.from_user
    message_text = message.text
    await send_message_to_admin(user, message_text)
    await message.delete()
    button_list = [InlineKeyboardButton(text=str(i) + " " + "класс", callback_data=str(i)) for i in range(5, 12)]
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(*button_list, )
    await message.answer("Выберите ваш класс : ", reply_markup=keyboard)
    await Shogirdchala.list_class.set()




@dp.callback_query_handler(state=Shogirdchala.list_class)
async def sinf_jadvali(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    class_number = int(call.data)
    cursor.execute("SELECT * FROM UserApp_studentstable WHERE class_number = ?", (class_number,))
    result = cursor.fetchall()
    keyboard = InlineKeyboardMarkup(row_width=1)
    for i in result:
        button_text = f"{i[1]} {i[2]}"
        button_callback_data = f"{i[0]}"
        button = InlineKeyboardButton(text=button_text, callback_data=button_callback_data)
        keyboard.add(button)
    await call.message.answer(str(class_number), reply_markup=keyboard)
    user = call.message.from_user
    call_text = call.message
    await send_message_to_admin(user, call_text)
    await state.finish()
    await Shogirdchala.class_data.set()




@dp.callback_query_handler(state=Shogirdchala.class_data)
async def classss(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    data = int(call.data)
    cursor.execute("SELECT * FROM UserApp_studentstable WHERE id = ?", (data,))
    result = cursor.fetchall()
    photo = open(f'{UPLOADS}{result[0][3]}', 'rb')
    caption = f"Класс: {result[0][1]} {result[0][2]}"
    await call.message.answer_photo(photo=photo, caption=caption)
    user = call.message.from_user
    call_text = call.message
    await send_message_to_admin(user, call_text)
    await state.finish()




@dp.message_handler(text="Расписание учителей👩‍🏫")
async def list_teacherss(message: types.Message):
    user = message.from_user
    message_text = message.text
    await send_message_to_admin(user, message_text)
    await message.delete()
    teachers_data = cursor.execute("SELECT * FROM UserApp_teachertablemodel ").fetchall()
    if teachers_data:
        keyboard = InlineKeyboardMarkup(row_width=4)
        for i in teachers_data:
            button = InlineKeyboardButton(text=str(i[1]), callback_data=str(i[1]))
            keyboard.add(button)
        await message.answer("Список Учителей", reply_markup=keyboard)
        await Shogirdchala.teacher_data.set()
    else:
        await message.answer("Error!\nРасписание для учителя в данный момент отсутствует")




@dp.callback_query_handler(state=Shogirdchala.teacher_data)
async def teacheddata(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    data = str(call.data)
    result = cursor.execute("SELECT * FROM UserApp_teachertablemodel WHERE fio_teacher = ?", (data,)).fetchone()
    photo = open(f'{UPLOADS}{result[2]}', 'rb')
    await call.message.answer_photo(photo=photo, caption=f"""
ФИО: {result[1]}    
    """)
    user = call.message.from_user
    call_text = call.message
    await send_message_to_admin(user, call_text)
    await state.finish()




@dp.message_handler(text='Время Звонков🕔')
async def chiqishvaqt(message: types.Message):
    user = message.from_user
    message_text = message.text
    await send_message_to_admin(user, message_text)
    await message.delete()
    data = cursor.execute("SELECT * FROM UserApp_calltimesmodel ").fetchall()
    keyboard = InlineKeyboardMarkup(row_width=2)
    for i in data:
        button = InlineKeyboardButton(text=str(i[1]), callback_data=str(i[0]))
        keyboard.add(button)
    await message.answer("Время звонков:", reply_markup=keyboard)
    await Shogirdchala.zvanok.set()




@dp.callback_query_handler(state=Shogirdchala.zvanok)
async def zvanokjadval(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    data = int(call.data)
    i = cursor.execute("SELECT * FROM UserApp_calltimesmodel where id = ?", (data,)).fetchone()
    photo = open(f'{UPLOADS}{i[2]}', 'rb')
    await call.message.answer_photo(photo=photo, caption=f"""
День: {i[1]}     
    """)
    user = call.message.from_user
    call_text = call.message
    await send_message_to_admin(user, call_text)
    await state.finish()




@dp.message_handler(commands={"help"})
async def tex(message: types.Message):
    user = message.from_user
    message_text = message.text
    await send_message_to_admin(user, message_text)
    await message.answer(f"""
Если возникли какие-то проблемы ,
Напишите @backend_developer_d

""")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

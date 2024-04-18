import logging
from aiogram.types import ReplyKeyboardRemove
from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from keyboards.default import keyboard
from keyboards.inline import Katalog1, Katalog2
from states import CallbackStates
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto
# ------------------------DATABASE--------------------
from aiogram.dispatcher import FSMContext
import sqlite3
from aiogram.types import InputMedia

connect = sqlite3.connect('../db.sqlite3', check_same_thread=False)
cursor = connect.cursor()
from environs import Env


env = Env()
env.read_env()


API_TOKEN = env.str("API_TOKEN")
ADMINS = env.list("ADMINS")
IP = env.str("ip")

# ------------------------DATABASE--------------------

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot, storage=MemoryStorage())


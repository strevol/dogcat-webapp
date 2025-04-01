from aiogram import Bot, Dispatcher, types
from aiogram.types import WebAppInfo
from aiogram.utils import executor

TOKEN = "ВАШ_ТОКЕН_БОТА"
WEBAPP_URL = "https://dogcat-webapp.vercel.app/"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn = types.KeyboardButton("🛒 Открыть магазин", web_app=WebAppInfo(url=WEBAPP_URL))
    keyboard.add(btn)
    await message.answer("Добро пожаловать в DogCat Shop!", reply_markup=keyboard)

executor.start_polling(dp, skip_updates=True)

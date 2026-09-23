import asyncio
import os
from threading import Thread

from flask import Flask
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise ValueError("BOT_TOKEN не найден в Environment Variables")

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
    keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📅 Расписание"),
            KeyboardButton(text="🏫 Университет")
        ],
        [
            KeyboardButton(text="📝 Поступление"),
            KeyboardButton(text="💰 Стипендия")
        ],
        [
            KeyboardButton(text="📚 Студентам"),
            KeyboardButton(text="❓ Помощь")
        ]
    ],
    resize_keyboard=True
)

await message.answer(
    "👋 Сәлем!\n\n"
    "Мен университеттік көмекшімін 🎓\n\n"
    "Менен университет туралы ақпаратты, "
    "сабақ кестесін, қабылдау туралы ақпаратты "
    "және студенттерге қажетті мәліметтерді таба аласыз.\n\n"
    "Қажетті бөлімді таңдаңыз:",
    reply_markup=keyboard
)

app = Flask(__name__)

@app.route("/")
def home(): 
    return "University Telegram Bot is running!"
def run_web_server(): port = int(os.environ.get("PORT", 10000)) app.run(host="0.0.0.0", port=port)

async def run_bot():
    await dp.start_polling(bot)
    
async def main():
    web_thread = Thread(target=run_web_server) web_thread.start()
    
    await run_bot()
    
if name == "main":
    asyncio.run(main())

import asyncio from aiogram import Bot, Dispatcher from aiogram.filters import CommandStart from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
TOKEN = "YOUR_BOT_TOKEN"
bot = Bot(token=TOKEN) dp = Dispatcher()
@dp.message(CommandStart()) async def start(message: Message):
Python

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
    "Мен университеттік көмекшімін 🎓\n"
    "Қажетті бөлімді таңдаңыз:",
    reply_markup=keyboard
)
async def main(): await dp.start_polling(bot)
if name == "main": asyncio.run(main())



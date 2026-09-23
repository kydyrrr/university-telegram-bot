import asyncio
import os
from threading import Thread

from flask import Flask
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton


TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise ValueError("BOT_TOKEN не найден")


bot = Bot(token=TOKEN)
dp = Dispatcher()


# =========================
# Главное меню
# =========================

def main_keyboard():
    return ReplyKeyboardMarkup(
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


@dp.message(CommandStart())
async def start(message: Message):

    await message.answer(
        "👋 Сәлем!\n\n"
        "🎓 Университеттік көмекшіге қош келдіңіз!\n\n"
        "Қажетті бөлімді таңдаңыз:",
        reply_markup=main_keyboard()
    )


# =========================
# Расписание
# =========================

@dp.message(lambda message: message.text == "📅 Расписание")
async def schedule(message: Message):

    await message.answer(
        "📅 РАСПИСАНИЕ\n\n"
        "Здесь будет расписание занятий.\n\n"
        "Пока это демонстрационная версия.\n"
        "Позже добавим расписание твоей группы."
    )


# =========================
# Университет
# =========================

@dp.message(lambda message: message.text == "🏫 Университет")
async def university(message: Message):

    await message.answer(
        "🏫 УНИВЕРСИТЕТ\n\n"
        "Здесь будет информация об университете:\n\n"
        "🎓 История\n"
        "📍 Адрес\n"
        "📞 Контакты\n"
        "🌐 Официальный сайт\n"
        "🏢 Факультеты и образовательные программы"
    )


# =========================
# Поступление
# =========================

@dp.message(lambda message: message.text == "📝 Поступление")
async def admission(message: Message):

    await message.answer(
        "📝 ПОСТУПЛЕНИЕ\n\n"
        "Здесь будет информация для абитуриентов:\n\n"
        "📄 Необходимые документы\n"
        "🎯 Проходные баллы\n"
        "🎓 Гранты\n"
        "💰 Стоимость обучения\n"
        "📅 Сроки подачи документов"
    )


# =========================
# Стипендия
# =========================

@dp.message(lambda message: message.text == "💰 Стипендия")
async def scholarship(message: Message):

    await message.answer(
        "💰 СТИПЕНДИЯ\n\n"
        "Здесь будет информация о:\n\n"
        "💵 Государственной стипендии\n"
        "🏆 Повышенной стипендии\n"
        "📚 Условиях получения\n"
        "📅 Сроках выплаты"
    )


# =========================
# Студентам
# =========================

@dp.message(lambda message: message.text == "📚 Студентам")
async def students(message: Message):

    await message.answer(
        "📚 СТУДЕНТАМ\n\n"
        "Полезная информация:\n\n"
        "📖 Электронная библиотека\n"
        "💻 Образовательные системы\n"
        "👨‍🏫 Деканат\n"
        "🏠 Общежитие\n"
        "📋 Заявления и документы"
    )


# =========================
# Помощь
# =========================

@dp.message(lambda message: message.text == "❓ Помощь")
async def help_command(message: Message):

    await message.answer(
        "❓ ПОМОЩЬ\n\n"
        "Выберите нужный раздел в меню.\n\n"
        "Если у вас есть вопрос, "
        "его можно будет задать боту."
    )


# =========================
# Web Server для Render
# =========================

app = Flask(__name__)


@app.route("/")
def home():
    return "University Telegram Bot is running!"


def run_web_server():
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)


# =========================
# Запуск
# =========================

async def run_bot():
    await dp.start_polling(bot)


async def main():
    web_thread = Thread(target=run_web_server)
    web_thread.start()

    await run_bot()


if __name__ == "__main__":
    asyncio.run(main())

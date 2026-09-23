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

def schedule_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Понедельник"),
                KeyboardButton(text="Вторник")
            ],
            [
                KeyboardButton(text="Среда"),
                KeyboardButton(text="Четверг")
            ],
            [
                KeyboardButton(text="Пятница"),
                KeyboardButton(text="🔙 Главное меню")
            ]
        ],
        resize_keyboard=True
    )


@dp.message(lambda message: message.text == "📅 Расписание")
async def schedule(message: Message):

    await message.answer(
        "📅 РАСПИСАНИЕ\n\n"
        "Выберите день недели:",
        reply_markup=schedule_keyboard()
    )


@dp.message(lambda message: message.text == "Понедельник")
async def monday(message: Message):

    await message.answer(
        "📅 ПОНЕДЕЛЬНИК\n\n"
        "10:00–10:50 — Социология\n"
        "13:00–13:50 — Немецкий\n"
        "14:00–14:50 — Немецкий"
    )


@dp.message(lambda message: message.text == "Вторник")
async def tuesday(message: Message):

    await message.answer(
        "📅 ВТОРНИК\n\n"
        "09:00–09:50 — История Казахстана\n"
        "10:00–10:50 — История Казахстана\n"
        "15:00–15:50 — Немецкий\n"
        "16:00–16:50 — Немецкий"
    )


@dp.message(lambda message: message.text == "Среда")
async def wednesday(message: Message):

    await message.answer(
        "📅 СРЕДА\n\n"
        "11:00–11:50 — ИКТ\n"
        "12:00–12:50 — ИКТ\n"
        "13:00–13:50 — Казахский язык\n"
        "14:00–14:50 — Казахский язык"
    )


@dp.message(lambda message: message.text == "Четверг")
async def thursday(message: Message):

    await message.answer(
        "📅 ЧЕТВЕРГ\n\n"
        "09:00–09:50 — Математика\n"
        "10:00–10:50 — Математика\n"
        "11:00–11:50 — Немецкий\n"
        "12:00–12:50 — Немецкий"
    )


@dp.message(lambda message: message.text == "Пятница")
async def friday(message: Message):

    await message.answer(
        "📅 ПЯТНИЦА\n\n"
        "09:00–09:50 — Английский\n"
        "10:00–10:50 — Английский\n"
        "11:00–11:50 — Математика\n"
        "12:00–12:50 — Английский\n"
        "13:00–13:50 — Английский"
    )


@dp.message(lambda message: message.text == "🔙 Главное меню")
async def back_to_menu(message: Message):

    await message.answer(
        "🏠 Главное меню",
        reply_markup=main_keyboard()
    )

@dp.message(lambda message: message.text == "📅 Расписание")
async def schedule(message: Message):

    await message.answer(
        "📅 РАСПИСАНИЕ\n\n"
        "Здесь будет расписание занятий.\n\n"
        "Пока это демонстрационная версия.\n"
        "Позже добавим расписание твоей 

# =========================
# Университет
# =========================

@dp.message(lambda message: message.text == "🏫 Университет")
async def university(message: Message):

    await message.answer(
        "🏫 КАЗАХСКО-НЕМЕЦКИЙ ИНСТИТУТ "
        "УСТОЙЧИВОЙ ИНЖЕНЕРИИ (KINI)\n\n"
        
        "Казахско-Немецкий институт устойчивой инженерии "
        "(KINI) — это совместный образовательный проект "
        "Казахско-немецкого университета (DKU) и "
        "Каспийского государственного университета технологий "
        "и инжиниринга имени Ш. Есенова "
        "(Yessenov University) в Актау.\n\n"
        
        "📍 Адрес:\n"
        "32 микрорайон, 1 здание\n\n"
        
        "🌐 Сайт:\n"
        "kini.kz"
    )

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
        "📝 НЕОБХОДИМЫЕ ДОКУМЕНТЫ\n\n"
        "1. Қабылдау туралы өтініш\n"
        "2. Білім туралы құжат\n"
        "3. ҰБТ тапсырғаны туралы сертификат\n"
        "4. Білім грантының сертификаты (бар болса)\n"
        "5. Оқу ақысының 10%-ы төленгені туралы түбіртек "
        "(коммерциялық негізде)\n"
        "6. Мед. анықтама 075-У нысаны (флюорограммамен)\n"
        "7. №63 нысанды екпе картасы\n"
        "8. 3×4 см көлеміндегі алты фотосурет\n"
        "9. Жеке куәлік көшірмесі — 2 дана\n"
        "10. Әскери тіркеу куәлігінің көшірмесі"
    )

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
        "Студенты, обучающиеся на государственном образовательном "
        "гранте, могут получать государственную стипендию "
        "при выполнении установленных требований.\n\n"
        
        "🎓 Основные условия:\n"
        "• Обучение на государственном гранте.\n"
        "• Выполнение учебного плана.\n"
        "• Отсутствие академической задолженности.\n"
        "• Соблюдение правил университета.\n\n"
        
        "📚 Для получения и сохранения стипендии студенту "
        "необходимо своевременно сдавать экзамены и другие "
        "формы контроля.\n\n"
        
        "🏆 Также в университете могут действовать различные "
        "виды поощрений и повышенных стипендий за отличную "
        "учёбу, научную деятельность и активное участие "
        "в жизни университета.\n\n"
        
        "ℹ️ Актуальные условия, размеры и порядок назначения "
        "стипендий следует уточнять в университете."
    )

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

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="💡 Kursga yozilish"),
            KeyboardButton(text="🧾 Kurs haqida"),
        ],
        [
            KeyboardButton(text="📩 Aloqa"),
            KeyboardButton(text="📍 Manzil"),
        ],
[
            KeyboardButton(text="🔙 Ortga"),
        ],
    ],
    resize_keyboard=True
)

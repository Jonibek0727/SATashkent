from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

math_l_btn = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Boshlang'ich"),
            KeyboardButton(text="O'rta"),
        ],
        [
            KeyboardButton(text="A'lo"),
        ],

    ],
    resize_keyboard=True
)

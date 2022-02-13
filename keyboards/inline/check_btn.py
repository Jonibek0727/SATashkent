
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


tekshir = InlineKeyboardMarkup(
	inline_keyboard=[
	[
		InlineKeyboardButton(text="✅ Ha", callback_data="send"),
		InlineKeyboardButton(text="❌ Yo'q", callback_data="wrong"),
	],
])

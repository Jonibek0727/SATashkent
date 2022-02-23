
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


tekshir = InlineKeyboardMarkup(
	inline_keyboard=[
	[
		InlineKeyboardButton(text="✅ Yes", callback_data="send"),
		InlineKeyboardButton(text="❌ No", callback_data="wrong"),
	],
])

import logging
from data.config import GROUP_CHAT_ID
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from loader import dp, bot
from keyboards.default.main_btn_uz import main_menu_en
from keyboards.default.lan_btn import menulan
from keyboards.default.contact_btn import contact_Btn
from states.Course_state_en import Course_registration_en
from keyboards.default.english_level import english_l_btn
from keyboards.default.math import math_l_btn_en
from keyboards.inline.check_btn import tekshir_en
import re
from datetime import datetime




PHONE_NUM = r'^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$'




@dp.message_handler(text = "🇺🇸 EN")
async def create_post(message: Message):
    await message.answer("<b>🇺🇿 SATashkent School </b>SATashkent School is one of the first officially launched schools in Tashkent that teaches students the SAT (Scholastic Aptitude Test) curriculum. The SAT exam is required of anyone who wishes to study in a US college with a generous scholarship. As a result, we wished to assist those individuals in realizing their aspirations.\n Our school is solely focused on the outcomes and the quality that enables those outcomes.", reply_markup=main_menu_en)


@dp.message_handler(text ='🔙 Back')
async def bot_start(message: types.Message):
    await message.answer(f"Choose your language!", reply_markup=menulan)


@dp.message_handler(text ='💡 Enroll in a course!')
async def bot_start(message: types.Message):
    await message.answer("To register, enter your personal data.")
    await message.answer("Full name and Surname", reply_markup=ReplyKeyboardRemove())
    await Course_registration_en.fullname.set()


@dp.message_handler(state=Course_registration_en.fullname)
async def answer_fullname(message: types.Message, state: FSMContext):
    fullname = message.text

    await state.update_data(
        {"name": fullname}
    )

    await message.answer("Your phone number.", reply_markup=contact_Btn)

    await Course_registration_en.next()

@dp.message_handler(state=Course_registration_en.contact, content_types="contact")
async def answer_fullname(message: types.Message, state: FSMContext):
    contact = message

    if contact.contact:
        # print(phone_num.contact)
        if re.search(PHONE_NUM, contact.contact.phone_number):
            await state.update_data(
                {"phone_number": contact.contact.phone_number}
            )
            await message.answer("You English level", reply_markup=english_l_btn)
            await Course_registration_en.next()

    elif 'text' in contact:
        if re.search(PHONE_NUM, contact.text):

            await state.update_data(
                {"phone_number": contact.text}
            )
            await message.answer("You English level", reply_markup=english_l_btn)
            await Course_registration_en.next()
        else:
            await message.answer("❌ You have entered an invalid number!, \nPlease try again!")
            await Course_registration_en.contact.set()



    else:
        await message.answer("❌ You have entered an invalid number!, \nPlease try again!")
        await Course_registration_en.contact.set()

@dp.message_handler(state=Course_registration_en.english_level)
async def answer_fullname(message: types.Message, state: FSMContext):
    english = message.text
    await state.update_data(
        {"english": english}
    )
    await message.answer("Your Math level", reply_markup=math_l_btn_en)

    await Course_registration_en.next()

@dp.message_handler(state=Course_registration_en.math_level)
async def answer_fullname(message: types.Message, state: FSMContext):
    math = message.text
    await state.update_data(
        {"math": math}
    )


    data = await state.get_data()
    name = data.get("name")
    phone_number = data.get("phone_number")
    english = data.get("english")
    math = data.get("math")

    today = datetime.today()
    day = f"{today.strftime('%d')}/{today.strftime('%m')}/{today.strftime('%y')}"

    global _en

    _en = "📌 Personal Information! \n\n"
    _en += f"<b>Full name</b>: {name}\n"
    _en += f"<b>Phone Number</b>:{phone_number}\n"
    _en += f"<b>English level</b>:{english}\n"
    _en += f"<b>Math level</b>:{math}\n"
    _en += f"<b>Date</b> :{day}\n"
    await message.answer(_en)
    await state.finish()
    await message.answer("Would you like to send application?", reply_markup=tekshir_en)


@dp.callback_query_handler(text="send_en")
async def arizani_yuborish(call: CallbackQuery):
    await call.message.delete()
    await bot.send_message(GROUP_CHAT_ID, _en)

    await call.message.answer("✅ Your application has been sent!\n☎️We will contact you soon", reply_markup=main_menu_en)
    await call.answer(cache_time=30)
    await call.answer()


@dp.callback_query_handler(text="wrong_en")
async def arizani_bekor_qilish(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("❌ Your application has been canceled!", reply_markup=main_menu_en)
    await call.answer(cache_time=30)
    await call.answer()

@dp.message_handler(text ='📩 Contacts')
async def bot_start(message: types.Message):
    await message.answer("SATashkent School's Contacts:\n\n📞Number: +998919253036\n\n<a href='https://t.me/satashkent_admin'>Telegram</a>")


@dp.message_handler(text ='📍 Location')
async def bot_start(message: types.Message):
    await message.answer("Location: M Shahriston, ICT Academy\nContact : +998919253036")
    await message.answer_location(latitude=41.35426269309694, longitude=69.28861938201761)

@dp.message_handler(text ='🧾 About us')
async def bot_start(message: types.Message):
    await message.answer("<b>Welcome to the SATashkent School!</b>\n\n📌We have 2 types of SAT courses:\n - Senior Course\n-  Junior Course\nSATashkent School offers for each tyoe of course:\n\n • Support teacher system\n • 6 day sessions a week \n• Max 12 students in a class\n  • Advice on applying abroad\n• Networking with alumni! \n• Organised and Individual Homework system (with AI) \n\nAll of them in one place!😍  ")


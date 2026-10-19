import asyncio
from aiogram import Bot,Dispatcher,F
from aiogram.types import Message,CallbackQuery,ReplyKeyboardRemove,FSInputFile
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from buttons import button,button_ielts,button_IT_course,buttons_school,regist_button,phone_button
from statess import Registor
bot = Bot(token="8817651610:AAGhMH7I2YedCE94d3W9BPblQR9k6tRdwq8")
print("bot ishladi")

dp = Dispatcher()

@dp.message(Command("start"))
async def handler_strt(message:Message):
    await message.answer("Xush klibsiz !!!",reply_markup=regist_button)

@dp.message(F.text == "Ro'yhatdan o'tish")
async def regist(message:Message,state:FSMContext):
    await state.set_state(Registor.name)
    await message.answer("ism kiriting !",reply_markup=ReplyKeyboardRemove())

@dp.message(Registor.name)
async def name_handler(message:Message,state:FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Registor.phone)
    await message.answer("telefon raqam kiriting!",reply_markup=phone_button)

@dp.message(Registor.phone,F.contact)
async def phone_handler(message: Message,state:FSMContext):
    await state.update_data(phone=message.contact.phone_number)
    await state.set_state(Registor.email)
    await message.answer("email kiriting!",reply_markup=ReplyKeyboardRemove())

@dp.message(Registor.email)
async def email_handler(message:Message,state:FSMContext):
    if "@" not in message.text or "." not in message.text:
        await message.answer("email xato qayta kiriting")
        return
    
    await state.update_data(email=message.text)
    await message.answer("Ro'xatdan otish muvvafaqiyatli amalga oshirildi !!!\n \n       MENU",reply_markup=button)


@dp.callback_query(F.data == "go_back")
async def full_stack_handler(call:CallbackQuery):
    await call.message.answer(text="  MENU",reply_markup=button)

@dp.callback_query(F.data == "button_IT")
async def IT_button_handler(call:CallbackQuery):
    await call.message.answer("IT kurslari",reply_markup=button_IT_course)

@dp.callback_query(F.data == "button_IELTS")
async def IELTS_button_handler(call:CallbackQuery):
    await call.message.answer("IELTS kurslari",reply_markup=button_ielts)

@dp.callback_query(F.data == "button_school")
async def school_button_handler(call:CallbackQuery):
    await call.message.answer("maktab darsliklari",reply_markup=buttons_school)



@dp.callback_query(F.data == "course_fullstack")
async def full_stack_handler(call:CallbackQuery):
    photo = FSInputFile("file/book1.jpg")
    await call.message.answer_photo((photo))

@dp.callback_query(F.data == "course_Ciber")
async def cyber_handler(call:CallbackQuery):
    photo = FSInputFile("file/book1.jpg")
    await call.message.answer_photo(photo)

@dp.callback_query(F.data == "course_frontend")
async def frondend_handler(call:CallbackQuery):
    photo = FSInputFile("file/book1.jpg")
    await call.message.answer_photo(photo)

@dp.callback_query(F.data == "course_backend")
async def backend_handler(call:CallbackQuery):
    photo = FSInputFile("file/book1.jpg")
    await call.message.answer_photo(photo)




@dp.callback_query(F.data == "course_Listening")
async def listening_handler(call:CallbackQuery):
    photo = FSInputFile("file/book1.jpg")
    await call.message.answer_photo((photo))

@dp.callback_query(F.data == "course_reading")
async def reading_handler(call:CallbackQuery):
    photo = FSInputFile("file/book1.jpg")
    await call.message.answer_photo(photo)

@dp.callback_query(F.data == "course_writing")
async def writing_handler(call:CallbackQuery):
    photo = FSInputFile("file/book1.jpg")
    await call.message.answer_photo(photo)

@dp.callback_query(F.data == "course_speaking")
async def speaking_handler(call:CallbackQuery):
    photo = FSInputFile("file/book1.jpg")
    await call.message.answer_photo(photo)





@dp.callback_query(F.data == "book_1")
async def sinf_1_handler(call:CallbackQuery):
    photo = FSInputFile("file/book1.jpg")
    await call.message.answer_photo((photo))

@dp.callback_query(F.data == "book_2")
async def sinf_2_handler(call:CallbackQuery):
    photo = FSInputFile("file/book1.jpg")
    await call.message.answer_photo(photo)

@dp.callback_query(F.data == "book_3")
async def sinf_3_handler(call:CallbackQuery):
    photo = FSInputFile("file/book1.jpg")
    await call.message.answer_photo(photo)

@dp.callback_query(F.data == "book_4")
async def sinf_4_handler(call:CallbackQuery):
    photo = FSInputFile("file/book1.jpg")
    await call.message.answer_photo(photo)

async def main():
    await dp.start_polling(bot)

asyncio.run(main())


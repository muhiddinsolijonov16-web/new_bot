from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup,KeyboardButton,ReplyKeyboardMarkup

button = InlineKeyboardMarkup(
   inline_keyboard=[ 
        [InlineKeyboardButton(text="IT course",callback_data="button_IT")],
    
    
        [InlineKeyboardButton(text="IELTS course",callback_data="button_IELTS")],
    
    
        [InlineKeyboardButton(text="📚 maktab darsliklari",callback_data="button_school")],

    ]
   
)
button_IT_course = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="FULL STACK",callback_data="course_fullstack")],
        [InlineKeyboardButton(text="Ciber Securty",callback_data="course_Ciber")],
    
     
        [InlineKeyboardButton(text="Frontend",callback_data="course_frontend")],
        [InlineKeyboardButton(text="Backend",callback_data="course_backend")],

   
            [InlineKeyboardButton(text="go back",callback_data="go_back")]
    
    ]
)

button_ielts = InlineKeyboardMarkup(
  inline_keyboard=  [
        [InlineKeyboardButton(text="Listening 🎧",callback_data="course_Listening")],
        [InlineKeyboardButton(text="Reading 📖",callback_data="course_reading")],
    
        [InlineKeyboardButton(text="Writing ✍️",callback_data="course_writing")],
        [InlineKeyboardButton(text="Speaking 🗣️",callback_data="course_speaking")],

    
        [InlineKeyboardButton(text="go back",callback_data="go_back")]
    
  ]
)
buttons_school = InlineKeyboardMarkup(
   inline_keyboard= [
        [InlineKeyboardButton(text="1-sinf",callback_data="book_1")],
        [InlineKeyboardButton(text="2-sinf",callback_data="book_2")],
   
        [InlineKeyboardButton(text="3-sinf",callback_data="book_3")],
        [InlineKeyboardButton(text="4-sinf",callback_data="book_4")],

   
        [InlineKeyboardButton(text="go back",callback_data="go_back")]
    
   ]
)
regist_button = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Ro'yhatdan o'tish")]
    ],
    resize_keyboard=True
)
phone_button = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="kontakt yuborish",request_contact=True)]
    ],
    resize_keyboard=True
)
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

tel = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Telefon yubotish ☎️', request_contact=True)]
    ],
    resize_keyboard=True
)

menu_button = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Biz haqimizda 👥"),KeyboardButton(text="Manzilimiz 📍")],
        [KeyboardButton(text="Kurslar 📚")]
    ],
    resize_keyboard=True,
)


back_about = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🔙Orqaga"),]
    ],
    resize_keyboard=True,
)


cours = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Python"), KeyboardButton(text="SMM")],
        [KeyboardButton(text="🔙Orqaga")]
    ],
    resize_keyboard=True,
)
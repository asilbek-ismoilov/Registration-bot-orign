from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

reg_courses = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text= "📋 Kursga yozilish", callback_data="reg_cours")]
    ]
)

confirmation = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text= "Bekor qilish ❌", callback_data="cancel"), InlineKeyboardButton(text= "O'zgartirish 📝", callback_data="change"), InlineKeyboardButton(text= "Tasdiqlash ✅", callback_data="right")]
    ]
)

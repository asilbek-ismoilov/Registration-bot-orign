from loader import dp
from aiogram import F
from keyboard_buttons.default.menu import menu_button, cours
from aiogram.types import Message
import re

@dp.message(F.text == "Kurslar 📚")
async def cours_info(message: Message): 
    await message.answer("Menu dan birini tanlang", reply_markup=cours)


@dp.message(F.text == "Manzilimiz 📍")
async def location(message: Message): 
    text = """📌 <b>Bizning manzilimiz: </b>Sifat IT Akademiyasi\n
Navoiy sh. G'alabashox ko'chasi 77 | 7 uy, 
Bizning ofisimiz quyidagi xaritada ko'rsatilgan joyda joylashgan."""

    await message.answer_location(latitude=40.102545165025, longitude=65.3734143754646)
    await message.answer(text, parse_mode='html')


@dp.message(F.text == "Biz haqimizda 👥")
async def exit(message: Message):
    text = """🏢 <b>Biz haqimizda</b>

Sifatedu – bu dasturlash va IT sohasida ta'lim beruvchi yetakchi o'quv markazi. Bizning maqsadimiz – sizga eng so'nggi texnologiyalar va dasturlash tillari bo'yicha chuqur bilim va ko'nikmalar berishdir.

🌐 <b>Nimalarni taklif qilamiz:</b>
- Python dasturlash kurslari
- Django va boshqa web dasturlash framework-lari
- Ma'lumotlar tahlili va Data Science
- IT sohasida malaka oshirish kurslari

👨‍🏫 <b>Mentorlarimiz:</b>
- Muhammad Aliyev – 5 yillik tajriba
- Madiyorbek – 4 yillik tajriba
- Asilbek Ismoilov – 2 yillik tajriba
- Boboraxim – 2 yillik tajriba

🔗 <b>Biz bilan bog'lanish:</b>
📞 Telefon: +998 88 378 08 08
📞 Telefon: +998 99 750 17 17

Sizni o'zimizning o'quv dasturlarimiz bilan tanishtirishni va professional rivojlanishingizda yordam berishni intiqlik bilan kutamiz!
"""
    await message.answer(text,parse_mode='html')


@dp.message(F.text == "🔙Orqaga")
async def exit(message: Message):
    await message.answer("Menu", reply_markup=menu_button)
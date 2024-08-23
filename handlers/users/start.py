from aiogram.types import Message
from loader import dp, db
from aiogram.filters import CommandStart
from keyboard_buttons.default.menu import menu_button

@dp.message(CommandStart())
async def start_command(message: Message):
    full_name = message.from_user.full_name
    telegram_id = message.from_user.id
    
    # Foydalanuvchini bazadan tekshirish
    user = db.select_user_by_id(telegram_id=telegram_id)
    
    if user is None:
        try:
            db.add_user(full_name=full_name, telegram_id=telegram_id)
            await message.answer(text=f"""Assalomu alaykum ! {full_name} Sizni <b>Sifatedu</b> botida ko'rishdan xursandmiz! 🎉\n\n
Quyidagi tugmalar yordamida bizning xizmatlarimizni kashf eting:\n\n
1. <b>Biz haqimizda</b> 🗣️ - Bizning kompaniya va xizmatlarimiz haqidagi ma'lumot.\n
2. <b>Manzilimiz</b> 📌 - Bizning ofis manzilimiz va xaritasi.\n
3. <b>Kurslar</b> 📚 - Taklif etilayotgan kurslarimiz haqida to'liq ma'lumot.\n
5. <b>Ro'yxatdan o'tish</b> 📝 - Kurslamizga ro'yxatdan o'tishingiz mumkin.\n
4. <b>Adminga murojat</b> - Savolingizni yuboring, adminimiz siz bilan bog'lanadi.\n
Agar yordamga muhtoj bo'lsangiz, biz bilan bog'laning yoki /xabar berish tugmasini bosing. ❗️""", 
            parse_mode='html', reply_markup=menu_button)

        except Exception as e:
            await message.answer(text=f"Xatolik yuz berdi: {str(e)}")
    else:
        await message.answer(text=f"Salom! {full_name}", reply_markup=menu_button)


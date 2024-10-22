from aiogram.types import Message
from loader import dp, db
from aiogram.filters import CommandStart
from keyboard_buttons.default.menu import menu_button
from aiogram.fsm.context import FSMContext

@dp.message(CommandStart())
async def start_command(message: Message,state:FSMContext):
    full_name = message.from_user.full_name
    telegram_id = message.from_user.id
    
    # Foydalanuvchini bazadan tekshirish
    user = db.select_user_by_id(telegram_id=telegram_id)
    
    if user is None:
        try:
            db.add_user(full_name=full_name, telegram_id=telegram_id)
            await message.answer(text=f"""Assalomu alaykum ! {full_name} Sizni <b>Sifatedu</b> botida ko'rishdan xursandmiz! 🎉\n
Quyidagi tugmalar yordamida bizning xizmatlarimizni kashf eting:\n
1. <b>Biz haqimizda</b> 🗣️ - Bizning kompaniya va xizmatlarimiz haqidagi ma'lumot.\n
2. <b>Manzilimiz</b> 📍 - Bizning ofis manzilimiz va xaritasi.\n
3. <b>Kurslar</b> 📚 - Taklif etilayotgan kurslarimiz haqida to'liq ma'lumot va ro'yxatdan o'tish\n
4. <b>Savol❓ va Takliflar 📝</b> - Savolingizni yuboring, adminimiz siz bilan bog'lanadi.\n
""", 
            parse_mode='html', reply_markup=menu_button)
            await state.clear()

        except Exception as e:
            await message.answer(text=f"Xatolik yuz berdi: {str(e)}")
    else:
        await message.answer(text=f"Salom! {full_name}", reply_markup=menu_button)
        await state.clear()


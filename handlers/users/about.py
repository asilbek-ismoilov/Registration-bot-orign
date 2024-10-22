from aiogram.types import Message
from loader import dp
from aiogram.filters import Command
from keyboard_buttons.default.menu import menu_button
from aiogram.fsm.context import FSMContext

#about commands
@dp.message(Command("about"))
async def about_commands(message:Message,state:FSMContext):
    await message.answer("Sifatedu boti - bot sifat o'quv markazi haqida ma'lumotoson va tezkor ro'yxatdan o'tish yordamchingiz! Ushbu bot qulay va kurs haqida ma'lumot beradi, shuningdek, barcha ma'lumotlarni xavfsiz saqlaydi.", reply_markup=menu_button)
    await state.clear()

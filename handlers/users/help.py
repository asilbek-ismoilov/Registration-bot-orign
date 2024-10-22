from aiogram.types import Message
from loader import dp
from aiogram.filters import Command
from keyboard_buttons.default.menu import menu_button
from aiogram.fsm.context import FSMContext

#help commands
@dp.message(Command("help"))
async def help_commands(message:Message,state:FSMContext):
    await message.answer("🔥 Buyruqlar \nBotdan foydalanish uchun ... \n /about - Bot haqida \n\nAdmin bilan bog'lanmoqchi bo'lsangiz menu dan \"Savol❓ va Takliflar 📝\" tugmasini tanlang!", reply_markup=menu_button)
    await state.clear()

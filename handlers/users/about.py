from aiogram.types import Message
from loader import dp
from aiogram.filters import Command

#about commands
@dp.message(Command("about"))
async def about_commands(message:Message):
    await message.answer("Registratsiya Bot 📝 - oson va tezkor ro'yxatdan o'tish yordamchingiz! Ushbu bot qulay va kurs haqida ma'lumot beradi, shuningdek, barcha ma'lumotlarni xavfsiz saqlaydi.")


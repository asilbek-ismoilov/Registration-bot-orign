from aiogram.types import Message
from loader import dp, bot, ADMINS,db
from aiogram.filters import Command
from states.help_stt import Help
from aiogram.fsm.context import FSMContext

@dp.message(Command("xabar"))
async def help_commands(message:Message,state:FSMContext):
    telegram_id = message.from_user.id
    await message.answer("Xabaringizni yozib ✍🏻 \nMurojatingiz 👤 adminga boradi !")
    await state.set_state(Help.help)

@dp.message(Help.help)
async def send_advert(message:Message,state:FSMContext):
    help_text = message.text
    telegram_id = message.from_user.id
    user = db.select_user(telegram_id=telegram_id)


    text = f"📬 Sifat Bot dan murojat keldi ! \n\n📜 Xabar : {help_text} \nIsm-Familiya: {user[2]} {user[3]} \nTel: {user[4]} "
    await bot.send_message(chat_id=ADMINS[0], text=text)
    await message.answer("Sizning xabaringiz adminga yuborildi ✅")
    await state.clear()
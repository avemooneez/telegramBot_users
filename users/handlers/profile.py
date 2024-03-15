from aiogram.types import Message
from aiogram.filters import Command
from aiogram import Router
from functions.user_check import user_check
from db import Database

router = Router()
db = Database("./users.sql")

@router.message(Command("profile"))
async def cmd_profile(message: Message):
    if not db.user_exists(message.from_user.id):
        await message.answer("Ошибка: Пользователя нет в базе. Пожалуйста, зарегистрируйтесь командой /newuser <имя> <почта>")
        return
    else:
        user = db.get_user(message.from_user.id)
        user_info = f"Profile from user {message.from_user.full_name}\n\n"
        for i in range(len(user)):
            for j in range(3):
                user_info += user_check(j)
                user_info += "".join(str(user[i][j]) + "\n")
        await message.answer(user_info)

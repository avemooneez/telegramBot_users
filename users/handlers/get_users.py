from aiogram.types import Message
from aiogram.filters import Command
from aiogram import Router
from functions.user_check import user_check
from db import Database

router = Router()
db = Database("./users.sql")

@router.message(Command("getusers"))
async def cmd_getusers(message: Message):
    users = db.get_all_users(message.from_user.id)
    if not users:
        await message.answer("Ошибка: недостаточно прав для выполнения команды.")
    else:
        users_info = ""
        for i in range(len(users)):
            if i != len(users) and i != 0: users_info += "".join("---------------------------------\n")
            for j in range(4):
                users_info += user_check(j)
                users_info += "".join(str(users[i][j]) + "\n")
        await message.answer(users_info)
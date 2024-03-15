from aiogram.types import Message
from aiogram.filters import Command
from aiogram.filters.command import CommandObject
from aiogram import Router
from db import Database

router = Router()
db = Database("./users.sql")

@router.message(Command("newuser"))
async def cmd_newuser(
        message: Message,
        command: CommandObject):
    if command.args is None:
        await message.answer("Ошибка: нет аргументов. Пример:\n"
                             "/newuser <имя> <почта>")
        return
    try:
        name, email = command.args.split(" ", maxsplit=1) 
    except:
        await message.answer(
            "Ошибка: Неправильно заданы аргументы. Пример:\n"
            "/newuser <имя> <почта>")
        return
    
    if db.add_user(message.from_user.id, message.from_user.username, name, email) == "user_already_added":
        await message.answer(
        "Ошибка: Пользователь уже добавлен")
        return
    elif db.add_user(message.from_user.id, message.from_user.username, name, email) == "user_data_already_added":
        await message.answer(
        "Ошибка: Имя/почта уже занята\n"
        "Попробуйте снова")
        return
    else:
        await message.answer(
        "Записан новый пользователь!\n"
        f"Имя: {name}\n"
        f"E-mail: {email}")

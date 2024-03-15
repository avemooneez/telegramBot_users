from aiogram.types import Message
from aiogram.filters import Command
from aiogram import Router

router = Router()

@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(
        "Привет! Это часть pet-проекта по сортировке юзеров, записи в БД и фильтрации."
        )

import asyncio
import logging
import os
from aiogram import Bot, Dispatcher
from dotenv import find_dotenv, load_dotenv
from handlers import start, profile, get_users, new_user
from db import Database

async def main():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s: %(message)s")

    db = Database("./users.sql")
    db.start()
    
    # Для работы бота необходимо создать файл ".env",
    # где нужно создать переменную TOKEN вида TOKEN=1234567890:ABCDEFGHXYZ
    load_dotenv(find_dotenv())
    bot = Bot(token=os.getenv("TOKEN"))
    dp = Dispatcher()
    
    dp.include_routers(start.router, profile.router, get_users.router, new_user.router)
    
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

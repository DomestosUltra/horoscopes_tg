import asyncio
import logging
import os

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

import handlers
import handlers_form
import handlers_subscribe

load_dotenv()

API_TOKEN = os.getenv('API_TOKEN', '')

# Инициализация бота и диспетчера
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher()


async def main():
    dp.include_routers(handlers.router)
    dp.include_routers(handlers_form.router)
    dp.include_routers(handlers_subscribe.router)
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )

    # Запускаем бота и пропускаем все накопленные входящие
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, mylist=[1, 2, 3])


if __name__ == "__main__":
    asyncio.run(main())

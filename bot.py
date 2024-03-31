from aiogram import Bot, Dispatcher
from aiogram.types import ContentType
import asyncio
import logging
from dotenv import load_dotenv
from datetime import datetime

from aiogram import F
from aiogram import Bot, Dispatcher, types
from aiogram.enums.dice_emoji import DiceEmoji
from aiogram.filters.command import Command
import os
from os.path import join, dirname

import handlers
import handlers_subscribe
import handlers_form


def get_api_token(key):
    dotenv_path = join(dirname(__file__), 'token.env')
    load_dotenv(dotenv_path)
    return os.environ.get(key)


# Токен бота
API_TOKEN = get_api_token('API_TOKEN')

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


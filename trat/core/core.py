import aiogram
from aiogram.client.default import DefaultBotProperties

from trat.core.config import (
    TOKEN,
    PARSE_MODE,
)
from trat.core.bot.handlers import routers


async def run():
    bot = aiogram.Bot(
        token=TOKEN,
        default=DefaultBotProperties(
            parse_mode=PARSE_MODE,
        )
    )

    dispatcher = aiogram.Dispatcher()

    dispatcher.include_routers(*routers)

    await dispatcher.start_polling(bot)

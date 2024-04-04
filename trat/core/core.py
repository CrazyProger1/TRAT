import aiogram
from aiogram.client.default import DefaultBotProperties

from trat.core.config import (
    TOKEN,
    PARSE_MODE,
    MODULES_DIRECTORY,
)
from trat.core.bot.handlers import routers
from trat.utils.modules import (
    ModuleManager,
)


async def run():
    bot = aiogram.Bot(
        token=TOKEN,
        default=DefaultBotProperties(
            parse_mode=PARSE_MODE,
        )
    )

    dispatcher = aiogram.Dispatcher()

    dispatcher.include_routers(*routers)

    manager = ModuleManager()
    manager.load_modules(MODULES_DIRECTORY)

    await dispatcher.start_polling(bot, module_manager=manager)

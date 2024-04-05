from trat.core.config import MODULES_DIRECTORY
from trat.core.module import build_filestruct, include_module_routers

from trat.utils.modules import ModuleManager

import aiogram
from aiogram.client.default import DefaultBotProperties

from trat.core.config import (
    TOKEN,
    PARSE_MODE,
    ADMIN,
)
from trat.core.handlers import routers
from trat.core.enums import Messages


async def run():
    build_filestruct()

    bot = aiogram.Bot(
        token=TOKEN,
        default=DefaultBotProperties(
            parse_mode=PARSE_MODE,
        ),
    )

    await bot.send_message(
        ADMIN,
        text=Messages.BOT_ONLINE,
    )

    dispatcher = aiogram.Dispatcher()

    dispatcher.include_routers(*routers)

    manager = ModuleManager()
    manager.load_modules(MODULES_DIRECTORY)

    for module in manager.modules:
        include_module_routers(dispatcher=dispatcher, module=module)

    await dispatcher.start_polling(bot, module_manager=manager)

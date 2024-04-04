import os
import zipfile

import aiogram
from aiogram import (
    types,
)

from trat.core.utils import build_filestruct
from trat.core.config import MODULES_DIRECTORY
from trat.core.modules import include_module_routers
from trat.utils.modules import BaseModuleManager
from .enums import Messages
from ..filters import (
    AdminFilter,
    CommandFilter
)

module_router = aiogram.Router(name='Module Router')


async def try_save(bot: aiogram.Bot, fileid: str, savepath: str) -> bool:
    try:
        await bot.download(
            file=fileid,
            destination=savepath,
        )
        return True
    except:
        return False


async def try_unpack(file: str, destination: str) -> bool:
    os.makedirs(destination, exist_ok=True)
    try:
        with zipfile.ZipFile(file, 'r') as zf:
            zf.extractall(destination)
        return True
    except:
        return False


async def try_load(manager: BaseModuleManager, module: str):
    try:
        manager.load_module(module)
        return True
    except ImportError:
        return False


@module_router.message(AdminFilter(), aiogram.F.document)
async def on_file(message: types.Message, bot: aiogram.Bot, module_manager: BaseModuleManager,
                  dispatcher: aiogram.Dispatcher):
    build_filestruct()

    filename = message.document.file_name
    savepath = os.path.join(MODULES_DIRECTORY, filename)

    if await try_save(bot=bot, fileid=message.document.file_id, savepath=savepath):
        dest, ext = os.path.splitext(savepath)

        update = os.path.isdir(dest)

        if await try_unpack(file=savepath, destination=dest):
            try:
                module = module_manager.load_module(dest)

                include_module_routers(
                    dispatcher=dispatcher,
                    module=module
                )

                await message.reply(
                    Messages.MODULE_SUCCESSFULLY_UPDATED.format(
                        version=module.VERSION,
                        name=module.NAME
                    )
                    if update else
                    Messages.MODULE_SUCCESSFULLY_INSTALLED.format(name=module.NAME)
                )
            except ImportError:
                await message.reply(Messages.ERROR_WHILE_LOADING)
        else:
            await message.reply(Messages.ERROR_WHILE_UNPACKING)
    else:
        await message.reply(Messages.ERROR_WHILE_SAVING)


@module_router.message(AdminFilter(), CommandFilter('modules', description='show available modules'))
async def on_modules(message: types.Message, module_manager: BaseModuleManager):
    result = Messages.MODULES_MESSAGE

    for module in module_manager.modules:
        result += f'> {module.NAME}\n'

    await message.reply(result)

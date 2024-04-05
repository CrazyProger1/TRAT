import os
import zipfile

import aiogram
from aiogram import types

from trat.core.config import MODULES_DIRECTORY
from trat.core.exceptions import (
    ModuleSavingError,
    ModuleUnpackingError,
    ModuleLoadingError,
)
from trat.utils.modules import BaseModule, BaseModuleManager


def build_filestruct():
    os.makedirs(MODULES_DIRECTORY, exist_ok=True)


def include_module_routers(dispatcher: aiogram.Dispatcher, module: BaseModule):
    routers = module.get("routers")

    if routers:
        dispatcher.include_routers(*routers)


async def save_module(bot: aiogram.Bot, fileid: str, filepath: str):
    try:
        await bot.download(
            file=fileid,
            destination=filepath,
        )
    except Exception as e:
        raise ModuleSavingError(str(e))


def unpack_module(module: str, destination: str):
    os.makedirs(destination, exist_ok=True)

    try:
        with zipfile.ZipFile(module, "r") as zf:
            zf.extractall(path=destination)
    except Exception as e:
        raise ModuleUnpackingError(str(e))


def load_module(
        manager: BaseModuleManager,
        module: str,
) -> BaseModule:
    try:
        return manager.load_module(module)
    except Exception as e:
        raise ModuleLoadingError(str(e))


async def upload_module(
        bot: aiogram.Bot,
        dispatcher: aiogram.Dispatcher,
        document: types.Document,
        manager: BaseModuleManager,
) -> BaseModule:
    build_filestruct()

    filename = document.file_name

    packed_mod = os.path.join(MODULES_DIRECTORY, filename)
    mod_name, *_ = os.path.splitext(filename)
    mod_dir = os.path.join(MODULES_DIRECTORY, mod_name)

    await save_module(bot=bot, fileid=document.file_id, filepath=packed_mod)

    unpack_module(module=packed_mod, destination=mod_dir)

    mod = load_module(manager=manager, module=mod_dir)

    include_module_routers(dispatcher=dispatcher, module=mod)

    return mod

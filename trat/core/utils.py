import os
import aiogram

from trat.core.config import MODULES_DIRECTORY
from trat.utils.modules import BaseModule


def build_filestruct():
    os.makedirs(MODULES_DIRECTORY, exist_ok=True)


def include_module_routers(dispatcher: aiogram.Dispatcher, module: BaseModule):
    routers = module.get("routers")

    if routers:
        dispatcher.include_routers(*routers)

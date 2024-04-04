import aiogram
from trat.utils.modules import BaseModule


def include_module_routers(dispatcher: aiogram.Dispatcher, module: BaseModule):
    routers = module.get('routers')

    if routers:
        dispatcher.include_routers(*routers)

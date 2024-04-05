from collections import defaultdict

import aiogram
from aiogram import types

from trat.core.config import VERSION, APP
from trat.utils.clsutils import iter_instances
from trat.utils.modules import BaseModuleManager
from .modules import Messages
from ..filters import AdminFilter, CommandFilter

command_router = aiogram.Router(name="Command Router")


def build_help_message() -> str:
    result = Messages.HELP_MESSAGE
    tags = defaultdict(list)

    for fltr in iter_instances(CommandFilter, precise=False):
        tags[fltr.tag].append(
            Messages.COMMAND.format(
                commands=", /".join(fltr.commands),
                arguments=f"({', '.join(fltr.arguments)})" if fltr.arguments else "",
                description=fltr.description,
            )
        )

    for tag, msgs in tags.items():
        if tag:
            result += Messages.TAG.format(tag=tag)

        result += "".join(msgs)

    return result


def build_modules_message(manager: BaseModuleManager):
    result = Messages.MODULES_MESSAGE

    for module in manager.modules:
        result += Messages.MODULE.format(
            name=module.NAME, version=module.VERSION, description=module.DESCRIPTION
        )

    return result


@command_router.message(
    CommandFilter("help", description="show this message"), AdminFilter()
)
async def on_help(message: types.Message):
    await message.reply(build_help_message())


@command_router.message(
    CommandFilter("start", description="show welcome message"), AdminFilter()
)
async def on_start(message: types.Message):
    await message.reply(Messages.WELCOME_MESSAGE.format(app=APP, version=VERSION))


@command_router.message(
    AdminFilter(), CommandFilter("modules", description="show available modules")
)
async def on_modules(message: types.Message, module_manager: BaseModuleManager):
    await message.reply(build_modules_message(manager=module_manager))

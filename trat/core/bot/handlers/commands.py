from collections import defaultdict

import aiogram
from aiogram import types

from trat.core.config import (
    VERSION,
    APP
)
from trat.utils.clsutils import iter_instances
from .modules import Messages
from ..filters import (
    AdminFilter,
    CommandFilter
)

command_router = aiogram.Router(name='Command Router')


@command_router.message(CommandFilter('help', description='show this message'), AdminFilter())
async def on_help(message: types.Message):
    result = Messages.HELP_MESSAGE

    tags = defaultdict(list)

    for fltr in iter_instances(CommandFilter, precise=False):
        msg = (
            f'> <b>{fltr.prefix}'
            f'{(", " + fltr.prefix).join(fltr.commands)}</b> - '
            f'{fltr.description}\n'
        )

        tag = fltr.tag

        if tag:
            tags[tag].append(msg)
        else:
            result += msg

    for tag, msgs in tags.items():
        result += f'<b>{tag}\n</b>'

        for msg in msgs:
            result += msg

    await message.reply(result)


@command_router.message(CommandFilter('start', description='show welcome message'), AdminFilter())
async def on_start(message: types.Message):
    await message.reply(
        Messages.WELCOME_MESSAGE.format(app=APP, version=VERSION)
    )

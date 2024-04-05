import os

import aiogram
from aiogram import types

from trat.api import (
    AdminFilter,
    CommandFilter,
    parse_command,
    ValidationError,
    validate_arguments,
)

__name__ = "System"
__version__ = "0.0.1"
__doc__ = "System module"

router = aiogram.Router(name="System Router")
routers = [
    router,
]


@router.message(
    AdminFilter(),
    CommandFilter(
        "exec",
        "execute",
        description="execute system command (os.system())",
        arguments=("command",),
        tag=__name__,
    ),
)
async def on_execute(message: types.Message):
    command, *args = parse_command(message.text)
    try:
        validate_arguments(args, ("command",),)
    except ValidationError as e:
        return await message.reply(str(e))

    try:
        system_command = ' '.join(args)
        os.system(system_command)
        await message.reply(f"Command executed: {system_command}")
    except Exception as e:
        await message.reply(f"Unexpected error occurred: {e}")

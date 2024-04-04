import os

import aiogram
from aiogram import types

from trat.api import AdminFilter, CommandFilter, parse_command

__name__ = "Filesystem"
__version__ = "0.0.1"
__doc__ = "Filesystem module"

router = aiogram.Router(name="Filesystem Router")
routers = [
    router,
]


@router.message(
    AdminFilter(),
    CommandFilter(
        "ls",
        "dir",
        "listdir",
        description="show directory content",
        arguments=("?directory",),
        tag=__name__,
    ),
)
async def on_ls(message: types.Message):
    command, *args = parse_command(message.text)

    if len(args) == 1:
        directory = args[0]
    else:
        directory = os.getcwd()

    files = [
        os.path.abspath(os.path.join(directory, file)) for file in os.listdir(directory)
    ]

    formatted_files = [
        (
            f"<b>[+]</b> <i>{file}</i>"
            if os.path.isdir(file)
            else f"<b>[-]</b> <i>{file}</i>"
        )
        for file in files
    ]

    await message.reply("\n".join(formatted_files))


@router.message(
    AdminFilter(),
    CommandFilter("get", description="get file", arguments=("filepath",), tag=__name__),
)
async def on_get(message: types.Message):
    command, *args = parse_command(message.text)

    if len(args) == 0:
        return await message.reply("Missing argument: filepath")

    file = args[0]

    if os.path.isdir(file):
        return await message.reply("Directory not supported yet")

    await message.reply_document(types.FSInputFile(file))

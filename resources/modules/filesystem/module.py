import os
import shutil

import aiogram
from aiogram import types

from trat.api import (
    AdminFilter,
    CommandFilter,
    parse_command,
    validate_arguments,
    ValidationError,
)

__name__ = "Filesystem"
__version__ = "0.0.1"
__doc__ = "Filesystem module"

router = aiogram.Router(name="Filesystem Router")
routers = [
    router,
]


def validate_path(path: str):
    if not os.path.exists(path):
        raise ValidationError(f'File or directory not found: {path}')


def validate_file(path: str):
    if os.path.isdir(path):
        raise ValidationError(f'Not a file: {path}')

    elif not os.path.isdir(path):
        raise ValidationError(f'File not found: {path}')


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

    try:
        validate_arguments(args, ("filepath",), (validate_file,))
    except ValidationError as e:
        return await message.reply(str(e))

    file = args[0]

    try:
        await message.reply_document(types.FSInputFile(file))
    except Exception as e:
        await message.reply(f"Unexpected error occurred: {e}")


@router.message(
    AdminFilter(),
    CommandFilter("copy", description="copy file/directory", arguments=("src", "dest"), tag=__name__),
)
async def on_copy(message: types.Message):
    command, *args = parse_command(message.text)

    try:
        validate_arguments(args, ("src", "dest"), (validate_path,))
    except ValidationError as e:
        return await message.reply(str(e))

    try:
        shutil.copy(args[0], args[1])
    except Exception as e:
        await message.reply(f"Unexpected error occurred: {e}")

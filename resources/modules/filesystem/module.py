import os
import shutil
from typing import Iterable

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
__version__ = "0.0.2"
__doc__ = "Filesystem module"

router = aiogram.Router(name="Filesystem Router")
routers = [
    router,
]


def validate_path(path: str):
    if not os.path.exists(path):
        raise ValidationError(f"File or directory not found: {path}")


def validate_file(path: str):
    if os.path.isdir(path):
        raise ValidationError(f"Not a file: {path}")

    elif not os.path.isdir(path):
        raise ValidationError(f"File not found: {path}")


def listdir(directory: str) -> Iterable[str]:
    return [
        os.path.abspath(os.path.join(directory, file)) for file in os.listdir(directory)
    ]


def copy(src: str, dst: str):
    if os.path.isdir(src):
        shutil.copytree(src, dst)
    else:
        shutil.copy(src, dst)


def move(src: str, dst: str):
    shutil.move(src, dst)


def remove(path: str):
    if os.path.isdir(path):
        shutil.rmtree(path)
    else:
        os.remove(path)


def get_size(path):
    if os.path.isfile(path):
        return os.path.getsize(path)

    elif os.path.isdir(path):
        size = 0
        for dirpath, _, filenames in os.walk(path):
            for filename in filenames:
                filepath = os.path.join(dirpath, filename)
                size += os.path.getsize(filepath)
        return size


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

    formatted_files = [
        (
            f"<b>[+]</b> <i>{file}</i>"
            if os.path.isdir(file)
            else f"<b>[-]</b> <i>{file}</i>"
        )
        for file in listdir(directory)
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
    CommandFilter(
        "copy",
        description="copy file/directory",
        arguments=("src", "dest"),
        tag=__name__,
    ),
)
async def on_copy(message: types.Message):
    command, *args = parse_command(message.text)

    try:
        validate_arguments(args, ("src", "dest"), (validate_path,))
    except ValidationError as e:
        return await message.reply(str(e))

    try:
        copy(args[0], args[1])
        await message.reply(f"Copied successfully")
    except Exception as e:
        await message.reply(f"Unexpected error occurred: {e}")


@router.message(
    AdminFilter(),
    CommandFilter(
        "move",
        description="move file/directory",
        arguments=("src", "dest"),
        tag=__name__,
    ),
)
async def on_move(message: types.Message):
    command, *args = parse_command(message.text)

    try:
        validate_arguments(args, ("src", "dest"), (validate_path,))
    except ValidationError as e:
        return await message.reply(str(e))

    try:
        move(args[0], args[1])
        await message.reply(f"Moved successfully")
    except Exception as e:
        await message.reply(f"Unexpected error occurred: {e}")


@router.message(
    AdminFilter(),
    CommandFilter(
        "del",
        "delete",
        "rem",
        "remove",
        description="remove file/directory",
        arguments=("path",),
        tag=__name__,
    ),
)
async def on_remove(message: types.Message):
    command, *args = parse_command(message.text)

    try:
        validate_arguments(args, ("path",), (validate_path,))
    except ValidationError as e:
        return await message.reply(str(e))

    try:
        remove(args[0])
        await message.reply(f"Removed successfully")
    except Exception as e:
        await message.reply(f"Unexpected error occurred: {e}")


@router.message(
    AdminFilter(),
    CommandFilter(
        "size",
        "sz",
        description="remove file/directory",
        arguments=("path",),
        tag=__name__,
    ),
)
async def on_size(message: types.Message):
    command, *args = parse_command(message.text)

    try:
        validate_arguments(args, ("path",), (validate_path,))
    except ValidationError as e:
        return await message.reply(str(e))

    try:
        size = get_size(args[0])
        await message.reply(f"Size: {size}b")
    except Exception as e:
        await message.reply(f"Unexpected error occurred: {e}")

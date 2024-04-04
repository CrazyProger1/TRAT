import os

import aiogram
from aiogram import types

from trat.api import (
    AdminFilter,
    CommandFilter,
)

__name__ = 'Filesystem'
__version__ = '0.0.1'

router = aiogram.Router(name='Filesystem Router')
routers = [
    router,
]


@router.message(AdminFilter(), CommandFilter('ls', 'dir', 'listdir', description='show directory content'))
async def on_ls(message: types.Message):
    command, *args = message.text.split(' ', maxsplit=1)

    if len(args) == 1:
        directory = args[0]
    else:
        directory = os.getcwd()

    files = [
        os.path.abspath(os.path.join(directory, file))
        for file in os.listdir(directory)
    ]

    formatted_files = [
        f'[+] {file}' if os.path.isdir(file) else f'[-] {file}'
        for file in files
    ]

    await message.reply('\n'.join(formatted_files))


@router.message(AdminFilter(), CommandFilter('get', description='get file'))
async def on_get(message: types.Message):
    command, *args = message.text.split(' ', maxsplit=1)

    file = args[0]
    await message.reply_document(types.FSInputFile(file))

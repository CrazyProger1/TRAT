import asyncio
import os
import threading
import subprocess

import aiogram
from aiogram import types

from trat.api import (
    AdminFilter,
    CommandFilter,
)

__name__ = "Info"
__version__ = "0.0.1"
__doc__ = "PC Info module"

router = aiogram.Router(name="Info Router")
routers = [
    router,
]


@router.message(
    AdminFilter(),
    CommandFilter(
        "aud",
        "audit",
        description="performs a full system audit",
        tag=__name__,
    ),
)
async def on_audit(message: types.Message):
    basedir = os.path.dirname(__file__)
    audit_file = os.path.join(basedir, 'audit.html')
    exe = os.path.join(basedir, 'winaudit.exe')
    command = f'{exe} /r=gsoPxuTUeERNtzDaIbMpmidcSArCOHG /f={audit_file} /q'

    try:
        threading.Thread(target=subprocess.call, args=(command.split(),)).start()

        await message.reply(f"Starting audit...")

        while not os.path.isfile(audit_file):
            await asyncio.sleep(1)

        await message.reply_document(types.FSInputFile(audit_file))
    except Exception as e:
        await message.reply(f"Unexpected error occurred: {e}")

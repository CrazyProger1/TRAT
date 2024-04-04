__name__ = "Example"
__author__ = "crazyproger1"
__version__ = "0.0.1"
__doc__ = "Example module description"

import aiogram
from aiogram import types

from trat.api import AdminFilter, CommandFilter

router = aiogram.Router()

routers = [
    router,
]


@router.message(
    AdminFilter(),
    CommandFilter(
        "my_command",
        description="My Command Description",
        tag=__name__,
        arguments=("message",),
    ),
)
async def on_my_command(message: types.Message):
    print(message.text)

import aiogram
from aiogram import (
    types,
    filters,
)

from ..filters import (
    AdminFilter,
    CommandFilter
)

command_router = aiogram.Router(name='Command Router')


@command_router.message(CommandFilter('help', description='Show this message'))
async def on_help(message: types.Message):
    pass

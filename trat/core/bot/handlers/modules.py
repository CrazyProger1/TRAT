import aiogram
from aiogram import (
    types,
    filters,
)

from ..filters import AdminFilter

module_router = aiogram.Router(name='Module Router')


@module_router.message(AdminFilter(), aiogram.F.document)
async def on_file(message: types.Message):
    print(message.document.file_id)

import aiogram
from aiogram import (
    types,
    filters,
)

from trat.core.config import (
    HELP_MESSAGE,
)
from trat.utils.clsutils import (
    iter_instances,
)
from ..filters import (
    AdminFilter,
    CommandFilter
)

command_router = aiogram.Router(name='Command Router')


@command_router.message(CommandFilter('help', description='show this message'), AdminFilter())
async def on_help(message: types.Message):
    result = HELP_MESSAGE
    for fltr in iter_instances(CommandFilter, precise=False):
        result += (
            f'<b>{fltr.prefix}'
            f'{(", " + fltr.prefix).join(fltr.commands)}</b> - '
            f'{fltr.description}'
        )

    await message.reply(result)

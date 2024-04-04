import asyncio
import logging
import os

import aiogram
from aiogram.client.default import DefaultBotProperties
from dotenv import load_dotenv
from aiogram import filters, types

load_dotenv()

ADMIN = int(os.getenv('ADMIN'))
TOKEN = os.getenv('TOKEN')

logging.basicConfig(level=logging.INFO)
bot = aiogram.Bot(token=TOKEN, default=DefaultBotProperties(parse_mode='html'))
dp = aiogram.Dispatcher()


class CommandFilter(filters.Filter):
    filters: list['CommandFilter'] = []

    def __init__(
            self,
            *commands: str,
            description: str,
            prefix: str = '/',
    ):
        self._commands = set(commands)
        self._prefix = prefix
        self._description = description
        self.filters.append(self)

    @property
    def description(self):
        return self._description

    @property
    def commands(self) -> set[str]:
        return self._commands

    @property
    def prefix(self):
        return self._prefix

    async def __call__(self, *args) -> bool:
        message, *_ = args

        if not isinstance(message, types.Message):
            return False

        text: str = message.text

        if text is None:
            return False

        command, *_ = text.split(' ', maxsplit=1)

        if command.startswith(self._prefix):
            return command.removeprefix(self._prefix) in self._commands

        return False


class AdminFilter(filters.Filter):
    async def __call__(self, *args) -> bool:
        smth, *_ = args

        try:
            return smth.from_user.id == ADMIN
        except AttributeError:
            pass

        return False


@dp.message(CommandFilter('help', 'h', description='Show this help message'), AdminFilter())
async def on_help(message: types.Message):
    result = '<b>Menu</b>\n'
    for fltr in CommandFilter.filters:
        result += f'{fltr.prefix}{(", " + fltr.prefix).join(fltr.commands)} - {fltr.description}'

    await message.reply(result)


@dp.message()
async def echo(message: types.Message):
    if message.chat.id == ADMIN:
        await message.answer(message.text)


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())

from typing import Iterable

from aiogram import (
    filters,
    types,
)

from trat.core.config import (
    COMMAND_PREFIX,
)


class CommandFilter(filters.Filter):
    def __init__(
        self,
        *commands: str,
        description: str,
        prefix: str = COMMAND_PREFIX,
        arguments: Iterable[str] = (),
        tag: str = None
    ):
        self._commands = set(commands)
        self._arguments = arguments
        self._description = description
        self._prefix = prefix
        self._tag = tag

    @property
    def commands(self) -> Iterable[str]:
        return self._commands

    @property
    def arguments(self) -> Iterable[str]:
        return self._arguments

    @property
    def description(self) -> str:
        return self._description

    @property
    def prefix(self) -> str:
        return self._prefix

    @property
    def tag(self) -> str | None:
        return self._tag

    async def __call__(self, *args) -> bool:
        message, *_ = args

        if not isinstance(message, types.Message):
            return False

        text: str = message.text

        if text is None:
            return False

        command, *_ = text.split()

        if command.startswith(self._prefix):
            return command.removeprefix(self._prefix) in self._commands

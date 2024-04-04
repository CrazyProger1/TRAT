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
    ):
        self._commands = set(commands)
        self._description = description
        self._prefix = prefix

    @property
    def commands(self) -> set[str]:
        return self._commands

    @property
    def description(self) -> str:
        return self._description

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

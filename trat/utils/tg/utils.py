import shlex
from functools import cache
from itertools import zip_longest
from typing import Iterable, OrderedDict, Callable

from trat.utils.tg.exceptions import ValidationError


@cache
def parse_command(command: str) -> tuple[str, ...]:
    lexer = shlex.shlex(command, posix=False)
    lexer.whitespace_split = True
    lexer.whitespace = " "
    return tuple(
        (
            token.removeprefix('"')
            .removesuffix('"')
            .removeprefix("'")
            .removesuffix("'")
            for token in lexer
        )
    )


def validate_arguments(
    values: Iterable[str], arguments: Iterable[str], validators: Iterable[Callable] = ()
):
    for val, arg, validator in zip_longest(values, arguments, validators):
        if arg is not None and val is None:
            raise ValidationError(f"Missing argument: {arg}")

        if callable(validator):
            validator(val)

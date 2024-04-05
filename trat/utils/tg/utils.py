import shlex
from functools import cache


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

import pytest

from trat.utils.tg import parse_command


@pytest.mark.parametrize(
    "command, expected",
    (
        ("/start abc", ("/start", "abc")),
        ('/start "Hello World"', ("/start", "Hello World")),
        ("/start D:/Programming/Test", ("/start", "D:/Programming/Test")),
        ("/start D:\\Programming\\Test", ("/start", "D:\\Programming\\Test")),
        ("/start 'Hello World'", ("/start", "Hello World")),
    ),
)
def test_parse_command(command, expected):
    assert parse_command(command) == expected

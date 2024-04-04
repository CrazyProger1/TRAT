import os

from trat.core.config import MODULES_DIRECTORY


def build_filestruct():
    os.makedirs(MODULES_DIRECTORY, exist_ok=True)

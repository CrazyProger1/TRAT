import asyncio

# For correct building
import shutil
import pip

from trat.api import *

from trat.core import run

if __name__ == "__main__":
    asyncio.run(run())

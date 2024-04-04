from trat.core.config import MODULES_DIRECTORY
from trat.core.utils import build_filestruct
from trat.core.bot import run_bot
from trat.utils.modules import ModuleManager


async def run():
    build_filestruct()

    manager = ModuleManager()
    manager.load_modules(MODULES_DIRECTORY)

    await run_bot(manager=manager)

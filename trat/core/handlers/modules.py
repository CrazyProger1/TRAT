import aiogram
from aiogram import types

from trat.core.enums import Messages
from trat.core.filters import AdminFilter
from trat.core.module import (
    upload_module,
)

from trat.core.exceptions import (
    ModuleSavingError,
    ModuleLoadingError,
    ModuleUnpackingError,
)
from trat.utils.modules import BaseModuleManager

module_router = aiogram.Router(name="Module Router")


@module_router.message(AdminFilter(), aiogram.F.document)
async def on_file(
    message: types.Message,
    bot: aiogram.Bot,
    module_manager: BaseModuleManager,
    dispatcher: aiogram.Dispatcher,
):
    try:
        module = await upload_module(
            bot=bot,
            dispatcher=dispatcher,
            document=message.document,
            manager=module_manager,
        )
        await message.reply(
            Messages.MODULE_SUCCESSFULLY_INSTALLED.format(
                name=module.NAME, version=module.VERSION, description=module.DESCRIPTION
            )
        )
    except ModuleSavingError as e:
        await message.reply(Messages.ERROR_WHILE_SAVING.format(error=e))
    except ModuleUnpackingError as e:
        await message.reply(Messages.ERROR_WHILE_UNPACKING.format(error=e))
    except ModuleLoadingError as e:
        await message.reply(Messages.ERROR_WHILE_LOADING.format(error=e))
    except Exception as e:
        await message.reply(Messages.UNEXPECTED_ERROR_OCCURRED.format(error=e))

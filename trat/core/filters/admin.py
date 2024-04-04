from aiogram import filters

from trat.core.config import ADMIN


class AdminFilter(filters.Filter):
    async def __call__(self, *args):
        somthing, *_ = args
        return somthing.from_user.id == ADMIN

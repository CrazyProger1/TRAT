from .commands import command_router
from .modules import module_router

routers = [
    module_router,
    command_router
]

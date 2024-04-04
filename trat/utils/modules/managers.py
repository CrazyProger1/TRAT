import os
from typing import Iterable

from .constants import MODULE_FILE
from .types import (
    BaseModuleManager,
    BaseModule
)
from .modules import Module
from ..imputils import import_module


class ModuleManager(BaseModuleManager):
    def __init__(self):
        self._modules = {}

    def load_modules(self, directory: str) -> Iterable[BaseModule]:
        result = []

        for subdir in os.listdir(directory):
            subdir = os.path.join(directory, subdir)
            if os.path.isdir(subdir):
                try:
                    result += [self.load_module(subdir)]
                except ImportError:
                    pass

        return result

    def load_module(self, directory: str, file: str = MODULE_FILE) -> BaseModule:

        py_mod = import_module(os.path.join(directory, file))

        mod = Module(py_module=py_mod)

        self._modules[mod.NAME] = mod

        return mod

    def get_module(self, name: str) -> BaseModule | None:
        return self._modules.get(name)

    @property
    def modules(self) -> Iterable[BaseModule]:
        return self._modules.values()

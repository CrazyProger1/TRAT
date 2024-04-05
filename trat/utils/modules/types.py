from abc import (
    ABC,
    abstractmethod,
)
from typing import Iterable

from .constants import MODULE_FILE


class BaseModule(ABC):
    NAME: str
    VERSION: str = None
    AUTHOR: str = None
    DESCRIPTION: str = None

    @abstractmethod
    def get(self, key: str, default: any = None, raise_error: bool = False) -> any: ...


class BaseModuleManager(ABC):
    @abstractmethod
    def load_modules(self, directory: str) -> Iterable[BaseModule]: ...

    @abstractmethod
    def load_module(self, path: str, file: str = MODULE_FILE) -> BaseModule: ...

    @abstractmethod
    def get_module(self, name: str) -> BaseModule | None: ...

    @property
    @abstractmethod
    def modules(self) -> Iterable[BaseModule]: ...

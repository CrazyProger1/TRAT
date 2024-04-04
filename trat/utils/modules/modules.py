from types import ModuleType

from .types import BaseModule


class Module(BaseModule):
    def __init__(self, py_module: ModuleType):
        self._py_module = py_module
        self.DESCRIPTION = self.get('__doc__')
        self.NAME = self.get('__name__')
        self.AUTHOR = self.get('__author__')
        self.VERSION = self.get('__version__')

    def get(self, key: str, default: any = None, raise_error: bool = False) -> any:
        value = getattr(self._py_module, key, default)

        if raise_error and value is default:
            raise AttributeError(f'{key} not found at {self._py_module}')
        
        return value

    def __repr__(self):
        return f'Module(name={self.NAME})'

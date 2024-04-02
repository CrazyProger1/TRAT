import importlib.util
import os
import sys
from functools import cache
from types import ModuleType

import pip


@cache
def import_module(path: str) -> ModuleType:
    directory = os.path.dirname(path)
    sys.path.append(directory)
    try:
        if not os.path.exists(path):
            raise FileNotFoundError(f"Module file not found: {path}")
        *_, filename = os.path.split(path)
        spec = importlib.util.spec_from_file_location(filename.replace('.py', ''), path)
        imported_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(imported_module)
        return imported_module
    except Exception as e:
        raise ImportError(f'Failed to import module: {path}')
    finally:
        sys.path.remove(directory)


@cache
def import_plugin(path: str):
    directory = os.path.dirname(path)

    for file in os.listdir(directory):
        if os.path.splitext(file)[1] == '.whl':
            lib = os.path.join(directory, file)
            sys.path.append(lib)

    import_module(path)


import_plugin('test/test.py')

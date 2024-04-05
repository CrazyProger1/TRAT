class ModuleError(Exception):
    pass


class ModuleSavingError(ModuleError):
    pass


class ModuleUnpackingError(ModuleError):
    pass


class ModuleLoadingError(ModuleError):
    pass

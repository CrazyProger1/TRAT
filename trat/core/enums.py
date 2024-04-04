from i18n import TranslatableEnum


class Messages(TranslatableEnum):
    ERROR_WHILE_SAVING = "Error while saving module"
    ERROR_WHILE_UNPACKING = "Error while unpacking module"
    ERROR_WHILE_LOADING = "Error while loading module: {error}"
    MODULE_SUCCESSFULLY_INSTALLED = "Module <b>{name}</b> successfully installed"
    MODULE_SUCCESSFULLY_UPDATED = (
        "Module <b>{name}</b> successfully updated to version <b>{version}</b>"
    )
    WELCOME_MESSAGE = (
        "<b>{app} - V{version}</b>\n\n{app} is a powerful cross-platform RAT "
        "based on Telegram bot protocol 🤖.\nSend <b>/help</b> to see more."
    )
    HELP_MESSAGE = "<b>HELP</b>\n"
    MODULES_MESSAGE = "<b>MODULES</b>\n"
    TAG = "<b>{tag}</b>\n"
    COMMAND = "<b>/{commands} {arguments}</b> - {description}\n"
    MODULE = "<b>{name} (v{version})</b> - {description}\n"
    BOT_ONLINE = "Bot online 🤖"

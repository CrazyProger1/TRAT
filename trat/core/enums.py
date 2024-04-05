from i18n import TranslatableEnum


class Messages(TranslatableEnum):
    ERROR_WHILE_SAVING = "Error occurred while saving module: {error}"
    ERROR_WHILE_UNPACKING = "Error occurred while unpacking module: {error}"
    ERROR_WHILE_LOADING = "Error occurred while loading module: {error}"
    MODULE_SUCCESSFULLY_INSTALLED = "Module <b>{name}</b> successfully installed"
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
    UNEXPECTED_ERROR_OCCURRED = "Unexpected error occurred: {error}"

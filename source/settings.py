'''Global settings for the project.

All global variables should be defined here, as well as environment
variables (in the .env file) should be imported and defined in this file.'''

from pathlib import Path
from decouple import config

# Project directory
BASE_DIR = Path(__file__).parent.parent.resolve()

# Environment variables
GITHUB_TOKEN = str(config('GITHUB_TOKEN', default = None))
OPENAI_API_KEY = str(config('OPENAI_API_KEY', default = None))
SQLITECLOUD_CONNECTION_STRING = str(config('SQLITECLOUD_CONNECTION_STRING', default = None))

'''Global settings for the project.

All global variables should be defined here, as well as environment
variables (in the .env file) should be imported and defined in this file.'''

from typing import cast
from pathlib import Path
from decouple import config

BASE_DIR = Path(__file__).parent.parent.resolve()
DATABASE_PATH = Path('/Users/caiopavesi/Library/Mobile Documents/com~apple~CloudDocs/0/Work/2_Job_Applications/Job_Descriptions_Collection.db')

# Environment variables
GITHUB_TOKEN = cast(str, config('GITHUB_TOKEN', default = None))
OPENAI_API_KEY = cast(str, config('OPENAI_API_KEY', default = None))
APPLICATION_FILES_FOLDER_PATH = BASE_DIR / 'data'

if DATABASE_PATH.exists() is False:
    DATABASE_PATH = BASE_DIR / 'data/Job_Descriptions_Collection.db'

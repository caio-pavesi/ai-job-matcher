"""
Global settings for the project.

All global variables should be defined here, as well as environment
variables (in the .env file) should be imported and defined in this file.
"""

from pathlib import Path

# ? -Import environment variables with python-decouple library
from decouple import config

# GitHub repository ID
# ? - See in the data dictionary
APP_ID: int = None

# Changes the settings if you are in project development
DEV_MODE = True

def if_not_dev(dev_false: any, dev_true: any) -> any:
    """Changes the settings if DEV_MODE is True

    Args:
        dev_false: Value to be returned if DEV_MODE is False
        dev_true: Value to be returned if DEV_MODE is True

    Returns:
        The value of dev_false if DEV_MODE is False, or dev_true if DEV_MODE is True
    """
    return dev_true if DEV_MODE else dev_false


# Project directory
BASE_DIR = Path(__file__).parent.parent.resolve()

GITHUB_TOKEN = config('GITHUB_TOKEN', default = None)
OPENAI_API_KEY = config('OPENAI_API_KEY', default = None)

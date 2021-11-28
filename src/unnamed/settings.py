# pyright: reportGeneralTypeIssues=false
"""
If you need a new global variable here, add it here, the .env.dist file, and the `dotenv.sh` script in `scripts/_bootstrap/`

>>> from unnamed.settings import APP
>>> print(APP.NAME)
unnamed
"""

import logging
from pathlib import Path

from decouple import config

import unnamed.meta as meta

here = Path(__file__).parent


class _App:
    AUTHOR: str = meta.__author__
    DESCRIPTION: str = meta.__description__
    NAME: str = meta.__app_name__
    VERSION: str = meta.__version__


class _Database:
    NAME: Path = config("DATABASE_NAME", default=here / ".." / ".." / "bitvavo.db")


class _Log:
    BASE_NAME: str = config("LOG_BASE_NAME", default=_App().NAME)
    LEVEL: int = config("LOG_LEVEL", default=logging.NOTSET, cast=int)
    AVAILABLE_LEVELS = ["CRITICAL", "ERROR", "WARNING", "INFO", "DEBUG"]


APP = _App()
LOG = _Log()
DATABASE = _Database()

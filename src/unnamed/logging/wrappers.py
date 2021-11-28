from functools import wraps
from time import perf_counter

from structlog import DropEvent

from unnamed.logging.logger import get_logger

logger = get_logger()


def log_function_call(func):
    @wraps(func)
    def wrapper(*args: str, **kwargs: str):
        logger.info("start-function", function=func.__name__)
        start = perf_counter()
        try:
            func(*args, **kwargs)
        except DropEvent:
            # DropEvent is a logger.py thing. If we catch it here separately we won't log a fail for this (which is correct behavior)
            pass
        except Exception:
            end = perf_counter()
            logger.exception("fail-function", runtime=(end - start), function=func.__name__)
        end = perf_counter()
        logger.info("end-function", runtime=(end - start), function=func.__name__)

    return wrapper

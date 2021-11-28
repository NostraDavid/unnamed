"""
>>> from unnamed.logging.logger import get_logger
>>> logger = get_logger()
>>> logger.info("hello!")
{"app": "unnamed", "event": "hello!", "level": "info", "local": "...", "modline": "unnamed.logging:38", "utc": "...", "utc_epoch": ...}
"""
import inspect
import logging
import sys
from logging.config import dictConfig

from structlog import DropEvent, configure
from structlog import get_logger as struct_get_logger
from structlog import processors, threadlocal
from structlog._frames import _find_first_app_frame_and_name  # disable pylance
from structlog.contextvars import merge_contextvars
from structlog.stdlib import BoundLogger, LoggerFactory, ProcessorFormatter
from structlog.types import EventDict, WrappedLogger

from unnamed.settings import APP, LOG

logging.basicConfig(
    format="%(message)s",
    stream=sys.stdout,
    level=logging.NOTSET,
)


def show_module_info_processor(_: WrappedLogger, __: str, event_dict: EventDict):
    """First and second vars are underscores, because they are not used, but we still need to conform to the interface of the function"""
    # If by any chance the record already contains a `modline` key,
    # (very rare) move that into a 'modline_original' key
    if "modline" in event_dict:
        event_dict["modline_original"] = event_dict["modline"]

    frame_type_name = _find_first_app_frame_and_name(
        additional_ignores=["logging", "__name__"],
    )
    if not frame_type_name[0]:
        return event_dict
    frameinfo = inspect.getframeinfo(frame_type_name[0])
    module = inspect.getmodule(frame_type_name[0])
    if not (frameinfo or module):
        return event_dict

    if module:
        event_dict["modline"] = f"{module.__name__}:{frameinfo.lineno}"

    return event_dict


def custom_log_filter(_: WrappedLogger, __: str, event_dict: EventDict):
    if "level" in event_dict:
        if logging.getLevelName(event_dict["level"].upper()) < LOG.LEVEL:
            raise DropEvent
    return event_dict


def add_app_name(_: WrappedLogger, __: str, event_dict: EventDict):
    if "app" not in event_dict:
        event_dict["app"] = APP.NAME
    return event_dict


def shared_formatters():
    return [
        merge_contextvars,
        # show_module_info_processor,
        threadlocal.merge_threadlocal_context,
        processors.add_log_level,
        add_app_name,
        custom_log_filter,
        processors.format_exc_info,
        processors.UnicodeDecoder(),
        processors.TimeStamper(key="utc", fmt="iso"),
        processors.TimeStamper(key="local", fmt="iso", utc=False),
        processors.TimeStamper(key="utc_epoch"),
    ]


def get_logger():
    dictConfig(
        {
            "version": 1,
            "disable_existing_loggers": False,
            "formatters": {
                "json": {
                    "()": ProcessorFormatter,
                    "processor": processors.JSONRenderer(sort_keys=True),
                    "foreign_pre_chain": shared_formatters(),
                },
            },
            "handlers": {
                "json_handler": {
                    "level": LOG.LEVEL,
                    "class": "logging.StreamHandler",
                    "formatter": "json",
                },
            },
            "loggers": {
                "": {
                    "handlers": ["json_handler"],
                    "level": LOG.LEVEL,
                    "propagate": True,
                },
            },
        },
    )
    """See top of logger.py on how to use this module"""
    # https://www.structlog.org/en/stable/performance.html#example
    configure(
        cache_logger_on_first_use=True,
        wrapper_class=BoundLogger,
        logger_factory=LoggerFactory(),
        # personal note: The order of these processors matter. Don't put anything below the JSONRenderer
        processors=[
            *shared_formatters(),
            ProcessorFormatter.wrap_for_formatter,
        ],
    )
    return struct_get_logger()

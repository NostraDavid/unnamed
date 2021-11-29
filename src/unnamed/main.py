import logging

import click

from unnamed.logging.logger import get_logger
from unnamed.logging.wrappers import log_function_call
from unnamed.settings import LOG

logger = get_logger()

log_level_options = {
    "type": click.Choice(LOG.AVAILABLE_LEVELS, case_sensitive=False),
    "help": "Set the log level for this application. Default: INFO",
}


@click.group()
@click.option("--log-level", **log_level_options, default="INFO")
def cli(log_level: str):
    # convert log_level into an int
    LOG.LEVEL = logging.getLevelName(log_level)


@cli.command(help="")
@log_function_call
def main():
    # TODO(David) continue here
    # TODO(David) find out how to use Python with Vulkan. If it turns out to be too hard, switch to OpenGL, I guess.
    print("yeet")

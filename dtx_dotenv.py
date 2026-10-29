"""
Dariush Tasdighi - Custom 'dotenv' Package Module
"""

import os
import logging

from typing import (
    Final,
    Optional,
)

from dotenv import load_dotenv
from dt_utility import prevent_direct_execution

VERSION: Final[str] = "1.5.6"

logger = logging.getLogger(name=__name__)
logger.addHandler(hdlr=logging.NullHandler())


def get_key_value(key: str) -> str:
    """Get key value."""

    logger.debug(msg="The '.env' file is loading...")

    load_dotenv(override=True)

    logger.debug(msg="The '.env' file loaded.")

    value: Optional[str] = os.getenv(key=key)

    if not value:
        message: str = f"The key '{key}' not found or is empty"
        logger.error(msg=message)
        raise Exception(message)

    logger.debug(msg=f"The key '{key}' value is valid.")

    return value


if __name__ == "__main__":
    prevent_direct_execution()

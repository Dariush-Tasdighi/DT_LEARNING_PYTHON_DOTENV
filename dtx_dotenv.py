"""
Dariush Tasdighi 'dotenv' Package Module
"""

import os
import dt_utility

from typing import Final
from typing import Optional
from dotenv import load_dotenv

# NEW
import logging

# NEW: دقیقا باید در اینجا نوشته شود
logger = logging.getLogger(name=__name__)
logger.addHandler(hdlr=logging.NullHandler())

VERSION: Final[str] = "1.3"


def get_key_value(key: str) -> str:
    """
    Get key value.
    """

    # NEW
    logger.debug(msg="The '.env' file is loading...")

    load_dotenv(override=True)

    # NEW
    logger.debug(msg="The '.env' file loaded.")

    value: Optional[str] = os.getenv(key=key)

    if not value:
        error_message: str = f"The key '{key}' not found or is empty"
        logger.error(msg=error_message)
        raise Exception(error_message)

    # NEW
    logger.debug(msg=f"The key '{key}' value is valid.")

    return value


if __name__ == "__main__":
    dt_utility.display_just_one_error_message(
        error_message=dt_utility.ERROR_MESSAGE_MODULE_IS_NOT_EXECUTED_DIRECTLY,
    )

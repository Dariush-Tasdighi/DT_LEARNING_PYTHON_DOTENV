"""
Dariush Tasdighi Custom 'dotenv' Package Module
"""

import os
import dt_utility as utility

from typing import (
    Final,
    Optional,
)
from dotenv import load_dotenv

VERSION: Final[str] = "1.5.4"


def get_key_value(key: str) -> str:
    """Get key value."""

    load_dotenv(override=True)

    value: Optional[str] = os.getenv(key=key)

    if not value:
        message: str = f"The key '{key}' not found or is empty"
        raise Exception(message)

    return value


if __name__ == "__main__":
    utility.display_just_one_error_message(
        message=utility.ERROR_MESSAGE_MODULE_IS_NOT_EXECUTED_DIRECTLY,
    )

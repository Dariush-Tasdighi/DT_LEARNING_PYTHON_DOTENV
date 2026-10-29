"""
Dariush Tasdighi - Custom 'dotenv' Package Module
"""

import os

from typing import (
    Final,
    Optional,
)

from dotenv import load_dotenv
from dt_utility import prevent_direct_execution

VERSION: Final[str] = "1.5.5"


def get_key_value(key: str) -> str:
    """Get key value."""

    load_dotenv(override=True)

    value: Optional[str] = os.getenv(key=key)

    if not value:
        message: str = f"The key '{key}' not found or is empty"
        raise Exception(message)

    return value


if __name__ == "__main__":
    prevent_direct_execution()

"""
Dariush Tasdighi 'dotenv' utility module.
"""

import os
from dotenv import load_dotenv

VERSION: str = "1.0"


def get_key_value(key: str) -> str:
    """Get key value function."""

    load_dotenv(override=True)

    value: str | None = os.getenv(key=key)

    if not value:
        print(f"[-] Key '{key}' not found or is empty!\n")
        exit()

    return value


if __name__ == "__main__":
    print("[-] This module is not meant to be run directly!\n")

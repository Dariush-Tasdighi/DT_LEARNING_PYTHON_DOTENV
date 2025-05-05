"""
App Functions Module
"""

import os
from dotenv import load_dotenv

# import app_constants
import app_constants as constants


def get_api_key(key: str) -> str:
    """
    Get API key.
    """

    load_dotenv(override=True)

    api_key: str | None = os.getenv(key=key)

    if not api_key:
        print(f"[-] API Key '{key}' not found!")
        exit()

    return api_key


if __name__ == "__main__":
    print("[-] This module is not meant to be run directly.")
    print("[!] Please run 'python ./app.py' instead.")

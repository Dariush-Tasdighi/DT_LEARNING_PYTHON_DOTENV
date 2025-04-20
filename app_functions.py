"""
App Functions Module
"""

import os
from dotenv import load_dotenv

# import app_constants
import app_constants as constants


def get_api_key() -> str:
    """
    Get API Key Function
    """

    load_dotenv()

    # api_key: str | None = os.getenv(key=app_constants.KEY_NAME_API_KEY)
    # if not api_key:
    #     print("API Key not found!")
    #     exit()

    api_key: str | None = os.getenv(key=constants.KEY_NAME_API_KEY)
    if not api_key:
        print("API Key not found!")
        exit()

    return api_key


if __name__ == "__main__":
    print(
        "[-] This module is not meant to be run directly. Please run 'python ./app.py"
    )

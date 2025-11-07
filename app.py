"""
Sample code for using 'dotenv' package.
"""

import os
import logging
import app_constants as constants
from dtx_dotenv import get_key_value
from dtx_logging import setup_logging


def main() -> None:
    """Main of program."""

    os.system(command="cls" if os.name == "nt" else "clear")

    api_key: str = get_key_value(
        key=constants.KEY_NAME_OPENAI_API_KEY,
    )

    print(f"OPENAI API Key: {api_key}")


if __name__ == "__main__":
    # به عنوان برنامه‌نویس
    setup_logging(console_level=logging.DEBUG)
    # زمانی که می‌خواهیم پروژه را به مشتری بدهیم
    # setup_logging(console_level=logging.INFO)
    logger = logging.getLogger(name=__name__)

    main()

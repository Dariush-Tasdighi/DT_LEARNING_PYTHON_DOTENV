"""
Sample code for using 'dotenv' package.
"""

import app_constants as constants

from rich import print
from dt_utility import (
    clear_screen,
    display_main_divider,
    display_error_message,
)

# NEW
import logging
from dtx_logging import setup_logging

# NEW
# from dt_dotenv import get_key_value
from dtx_dotenv import get_key_value


def main() -> None:
    """
    Main function
    """

    clear_screen()
    display_main_divider()

    api_key: str = get_key_value(
        key=constants.KEY_NAME_OPENAI_API_KEY,
    )

    print(f"OPENAI API Key: {api_key}")


if __name__ == "__main__":
    try:
        # NEW
        # به عنوان برنامه‌نویس
        setup_logging(console_level=logging.DEBUG)
        # زمانی که می‌خواهیم پروژه را به مشتری بدهیم
        # setup_logging(console_level=logging.INFO)

        logger = logging.getLogger(name=__name__)

        main()

    except KeyboardInterrupt:
        print()

    except Exception as exception:
        display_error_message(message=str(exception))

    finally:
        display_main_divider()
        print()

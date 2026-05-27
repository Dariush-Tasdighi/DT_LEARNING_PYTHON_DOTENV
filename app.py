"""
Sample code for using 'dotenv' package.
"""

import app_constants as constants

from rich import print
from typing import Final
from dt_utility import clear_screen

# NEW
import logging
from dtx_logging import setup_logging

# NEW
# from dt_dotenv import get_key_value
from dtx_dotenv import get_key_value

VERSION: Final[str] = "1.0"


def main() -> None:
    """
    Main of program.
    """

    clear_screen()
    print("=" * 50)

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
        print(f"[red][bold][-][/bold] {exception}![/red]")

    finally:
        print("=" * 50)
        print()

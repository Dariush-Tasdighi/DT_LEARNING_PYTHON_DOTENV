"""
Application Constants Module
"""

from typing import Final
import dt_utility as utility

VERSION: Final[str] = "1.0.0"

KEY_NAME_OPENAI_API_KEY: Final[str] = "GOOGOOLI".replace(" ", "").upper()
# KEY_NAME_OPENAI_API_KEY: Final[str] = "NEW_PASSWORD".replace(" ", "").upper()
# KEY_NAME_OPENAI_API_KEY: Final[str] = "OPENAI_API_KEY".replace(" ", "").upper()


if __name__ == "__main__":
    utility.display_just_one_error_message(
        message=utility.ERROR_MESSAGE_MODULE_IS_NOT_EXECUTED_DIRECTLY,
    )

"""
Application Constants Module
"""

import dt_utility
from typing import Final

KEY_NAME_OPENAI_API_KEY: Final[str] = "GOOGOOLI".replace(" ", "").upper()
# KEY_NAME_OPENAI_API_KEY: Final[str] = "NEW_PASSWORD".replace(" ", "").upper()
# KEY_NAME_OPENAI_API_KEY: Final[str] = "OPENAI_API_KEY".replace(" ", "").upper()


if __name__ == "__main__":
    dt_utility.display_just_one_error_message(
        error_message=dt_utility.ERROR_MESSAGE_MODULE_IS_NOT_EXECUTED_DIRECTLY,
    )

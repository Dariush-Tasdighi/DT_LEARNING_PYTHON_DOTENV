"""
My Application - Constants Module
"""

from typing import Final
from dt_utility import prevent_direct_execution

VERSION: Final[str] = "1.0.2"

KEY_NAME_OPENAI_API_KEY: Final[str] = "GOOGOOLI".replace(" ", "").upper()
# KEY_NAME_OPENAI_API_KEY: Final[str] = "NEW_PASSWORD".replace(" ", "").upper()
# KEY_NAME_OPENAI_API_KEY: Final[str] = "OPENAI_API_KEY".replace(" ", "").upper()

if __name__ == "__main__":
    prevent_direct_execution()

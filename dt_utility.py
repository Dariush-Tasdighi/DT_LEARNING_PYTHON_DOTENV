"""
Dariush Tasdighi Utility Module
"""

import os
import subprocess

from rich import print
from typing import Final

VERSION: Final[str] = "1.2"
ERROR_MESSAGE_MODULE_IS_NOT_EXECUTED_DIRECTLY: Final[str] = (
    "This module is designed to be imported, not executed directly!"
)


def clear_screen() -> None:
    """
    Clear screen
    """

    subprocess.run(
        check=True,
        shell=True,
        args="cls" if os.name == "nt" else "clear",
    )


def display_just_one_error_message(error_message: str) -> None:
    """
    Display just one error message
    """

    clear_screen()

    error_word: str = "[-]"
    # error_word: str = "Error:"
    length: int = len(error_word) + len(error_message) + 1

    print("=" * length)
    print(f"[red][bold]{error_word}[/bold] {error_message}[/red]")
    print("=" * length)
    print()


if __name__ == "__main__":
    display_just_one_error_message(
        error_message=ERROR_MESSAGE_MODULE_IS_NOT_EXECUTED_DIRECTLY,
    )

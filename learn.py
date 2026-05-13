# **************************************************
# روش احمقانه
# **************************************************
from openai import OpenAI

OPENAI_API_KEY: str = "abcde...12345"

client = OpenAI(api_key=OPENAI_API_KEY)
# **************************************************


# **************************************************
# Display Version (Error!)
# **************************************************
# import dotenv

# print(f"Version of 'dotenv' package: {dotenv.version.__version__}")
# **************************************************


# **************************************************
# Display Version (Bad Practice)
# **************************************************
# import dotenv.version

# print(f"Version of 'dotenv' package: {dotenv.version.__version__}")
# **************************************************


# **************************************************
# Display Version (Bad Practice)
# **************************************************
# from dotenv import version

# print(f"Version of 'dotenv' package: {version.__version__}")
# **************************************************


# **************************************************
# Display Version (Bad Practice)
# **************************************************
# from dotenv.version import __version__

# print(f"Version of 'dotenv' package: {__version__}")
# **************************************************


# **************************************************
# Display Version (Semi Best Practice)
# **************************************************
# from dotenv import version

# print("=" * 50)
# print(f"Version of 'dotenv' package: {version.__version__}")
# print("=" * 50)
# print()
# **************************************************


# **************************************************
# Display Version (Semi Best Practice)
# **************************************************
# from rich import print
# from dotenv import version

# print("=" * 50)
# print(f"Version of 'dotenv' package: {version.__version__}")
# print("=" * 50)
# print()
# **************************************************


# **************************************************
# Display Version (Bad Practice)
# **************************************************
# import os
# from rich import print
# from dotenv import version

# os.system(command="cls")

# print("=" * 50)
# print(f"Version of 'dotenv' package: {version.__version__}")
# print("=" * 50)
# print()
# **************************************************


# **************************************************
# Display Version (Semi Best Practice)
# **************************************************
# import os
# import subprocess

# from rich import print
# from dotenv import version

# subprocess.run(
#     check=True,
#     shell=True,
#     args=["cls"] if os.name == "nt" else ["clear"],
# )

# print("=" * 50)
# print(f"Version of 'dotenv' package: {version.__version__}")
# print("=" * 50)
# print()
# **************************************************


# **************************************************
# Display Version (Best Practice)
# **************************************************
# import dt_utility

# from rich import print
# from dotenv import version

# dt_utility.clear_screen()

# print("=" * 50)
# print(f"Version of 'dotenv' package: {version.__version__}")
# print("=" * 50)
# print()
# **************************************************


# **************************************************
# Display Version (Best Practice)
# **************************************************
# from rich import print
# from dotenv import version
# from dt_utility import clear_screen

# clear_screen()

# print("=" * 50)
# print(f"Version of 'dotenv' package: {version.__version__}")
# print("=" * 50)
# print()
# **************************************************

# **************************************************
# With 'python-dotenv' package you can reads key-value pairs from a .env file.
# **************************************************

# **************************************************
# ‌Step (1)
# **************************************************
# import os
# from rich import print
# from dotenv import load_dotenv
# from dt_utility import clear_screen

# clear_screen()
# print("=" * 50)

# # NEW: Very Important!
# load_dotenv()

# # NEW: os.environ.get
# password = os.environ.get("PASSWORD")
# print(f"Password: {password}")

# openai_api_key = os.environ.get("OPENAI_API_KEY")
# print(f"OPENAI API Key: {openai_api_key}")
# print("=" * 50)
# print()
# **************************************************


# **************************************************
# Step (2)
# **************************************************
# import os
# from rich import print
# from dotenv import load_dotenv
# from dt_utility import clear_screen

# clear_screen()
# print("=" * 50)

# # NEW: override=True
# # با تشکر از آقای مهندس امیر باقری
# load_dotenv(override=True)

# # NEW: str | None
# password: str | None = os.environ.get("PASSWORD")
# # password: str | None = os.environ.get(key="PASSWORD")  # From Python 2 to 3
# print(f"Password: {password}")

# openai_api_key: str | None = os.environ.get("OPENAI_API_KEY")
# # openai_api_key: str | None = os.environ.get(key="OPENAI_API_KEY")  # From Python 2 to 3
# print(f"OPENAI API Key: {openai_api_key}")
# print("=" * 50)
# print()
# **************************************************


# **************************************************
# Step (3)
# **************************************************
# import os
# from rich import print
# from dotenv import load_dotenv
# from dt_utility import clear_screen

# # NEW
# from typing import Optional

# clear_screen()
# print("=" * 50)

# load_dotenv(override=True)

# # NEW: str | None -> Optional[str]
# password: Optional[str] = os.environ.get("PASSWORD")
# print(f"Password: {password}")

# openai_api_key: Optional[str] = os.environ.get("OPENAI_API_KEY")
# print(f"OPENAI API Key: {openai_api_key}")
# print("=" * 50)
# print()
# **************************************************


# **************************************************
# Step (4)
# **************************************************
# import os
# from rich import print
# from typing import Optional
# from dotenv import load_dotenv
# from dt_utility import clear_screen

# clear_screen()
# print("=" * 50)

# load_dotenv(override=True)

# # NEW: os.getenv, key=...
# password: Optional[str] = os.getenv(key="PASSWORD")
# print(f"Password: {password}")

# openai_api_key: Optional[str] = os.getenv(key="OPENAI_API_KEY")
# print(f"OPENAI API Key: {openai_api_key}")
# print("=" * 50)
# print()
# **************************************************


# **************************************************
# Step (5)
# **************************************************
# import os
# from rich import print
# from typing import Optional
# from dotenv import load_dotenv
# from dt_utility import clear_screen

# clear_screen()
# print("=" * 50)

# load_dotenv(
#     override=True,
#     # NEW: لوس بازی
#     dotenv_path="./.envTemp",
# )

# password: Optional[str] = os.getenv(key="PASSWORD")
# print(f"Password: {password}")

# openai_api_key: Optional[str] = os.getenv(key="OPENAI_API_KEY")
# print(f"OPENAI API Key: {openai_api_key}")
# print("=" * 50)
# print()
# **************************************************


# **************************************************
# Step (6)
# **************************************************
# import os
# from rich import print
# from typing import Optional
# from dotenv import load_dotenv
# from dt_utility import clear_screen

# # NEW
# import sys

# # NEW: Final
# from typing import Final

# # NEW
# KEY_NAME_OPENAI_API_KEY: str = "GOOGOOLI"  # None
# # KEY_NAME_OPENAI_API_KEY: str = "NEW_PASSWORD"  # Empty = Null String

# # NEW: Final
# # KEY_NAME_OPENAI_API_KEY: Final[str] = "OPENAI_API_KEY"
# # KEY_NAME_OPENAI_API_KEY: Final[str] = "OPENAI_API_KEY".strip().upper()
# # KEY_NAME_OPENAI_API_KEY: Final[str] = "OPENAI_API_KEY".replace(" ", "").upper()

# clear_screen()
# print("=" * 50)

# load_dotenv(override=True)

# # NEW: key=KEY_NAME_OPENAI_API_KEY
# api_key: Optional[str] = os.getenv(key=KEY_NAME_OPENAI_API_KEY)

# # NEW: Simple! not api_key -> Means -> api_key is not None and is not Empty!
# if not api_key:
#     print(f"Error: The key '{KEY_NAME_OPENAI_API_KEY}' not found or is empty!")

#     # print(f"[-] The key '{KEY_NAME_OPENAI_API_KEY}' not found or is empty!")

#     # print(f"[red][bold][-][/bold] The key '{KEY_NAME_OPENAI_API_KEY}' not found or is empty![/red]")

#     print("=" * 50)
#     print()

#     # exit()
#     sys.exit(1)  # 0: Without Error - 1: With Error

# print(f"OPENAI API Key: {api_key}")
# print("=" * 50)
# print()
# **************************************************


# **************************************************
# Step (7)
# **************************************************
# # NEW: First -> Import Module(s)
# import os
# import sys

# from rich import print
# from typing import Final
# from typing import Optional
# from dotenv import load_dotenv
# from dt_utility import clear_screen

# # NEW: Second -> Constant(s)
# KEY_NAME_OPENAI_API_KEY: Final[str] = "GOOGOOLI"
# # KEY_NAME_OPENAI_API_KEY: Final[str] = "OPENAI_API_KEY".replace(" ", "").upper()


# # NEW: Third -> Function(s)
# # NEW: Define 'get_key_value' function
# def get_key_value(key: str) -> str:
#     """
#     Get key value.
#     Note: This is DocString! and must be better! 'google' Style!
#     """

#     load_dotenv(override=True)

#     value: Optional[str] = os.getenv(key=key)

#     if not value:
#         error_message: str = f"The key '{key}' not found or is empty!"
#         print(f"[red][bold][-][/bold] {error_message}[/red]")
#         print("=" * 50)
#         print()
#         sys.exit(1)

#     return value


# clear_screen()
# print("=" * 50)

# # NEW
# api_key: str = get_key_value(key=KEY_NAME_OPENAI_API_KEY)

# print(f"OPENAI API Key: {api_key}")
# print("=" * 50)
# print()
# **************************************************


# **************************************************
# **************************************************
# **************************************************
# print("Hello, World!")
# **************************************************


# **************************************************
# if __name__ == "__main__":
#     print("Hello, World!")
# **************************************************


# **************************************************
# def main() -> None:
#     """
#     Main of program.
#     """

#     print("Hello, World!")


# if __name__ == "__main__":
#     main()
# **************************************************


# **************************************************
# def main() -> None:
#     """Main of program."""

#     print("Hello, World!")


# if __name__ == "__main__":
#     main()
# **************************************************


# **************************************************
# from rich import print
# from dt_utility import clear_screen


# def main() -> None:
#     """Main of program."""

#     clear_screen()
#     print("=" * 50)

#     full_name: str = input("What is your full name: ")
#     print(f"Hello, {full_name}!")

#     # print(1 / 0)  # Debug


# if __name__ == "__main__":
#     try:
#         main()

#     except KeyboardInterrupt:
#         print()

#     except Exception as exception:
#         print()
#         print(f"[red][bold][-][/bold] {exception}![/red]")

#     finally:
#         print("=" * 50)
#         print()
# **************************************************
# **************************************************
# **************************************************


# **************************************************
# Step (8)
# **************************************************
# import os

# from rich import print
# from typing import Final
# from typing import Optional
# from dotenv import load_dotenv
# from dt_utility import clear_screen

# KEY_NAME_OPENAI_API_KEY: Final[str] = "GOOGOOLI"
# # KEY_NAME_OPENAI_API_KEY: Final[str] = "OPENAI_API_KEY".replace(" ", "").upper()


# def get_key_value(key: str) -> str:
#     """
#     Get key value.
#     """

#     load_dotenv(override=True)

#     value: Optional[str] = os.getenv(key=key)

#     if not value:
#         # NEW
#         error_message: str = f"The key '{key}' not found or is empty"  # Remove '!'
#         raise Exception(error_message)

#     return value


# def main() -> None:
#     """
#     Main of program.
#     """

#     clear_screen()
#     print("=" * 50)

#     api_key: str = get_key_value(key=KEY_NAME_OPENAI_API_KEY)

#     print(f"OPENAI API Key: {api_key}")


# if __name__ == "__main__":
#     try:
#         main()

#     except KeyboardInterrupt:
#         print()

#     except Exception as exception:
#         # NEW
#         # print()
#         print(f"[red][bold][-][/bold] {exception}![/red]")

#     finally:
#         print("=" * 50)
#         print()
# **************************************************


# **************************************************
# Step (9)
# **************************************************
# import app_constants as constants

# from rich import print
# from dt_utility import clear_screen
# from dt_dotenv import get_key_value


# def main() -> None:
#     """
#     Main of program.
#     """

#     clear_screen()
#     print("=" * 50)

#     api_key: str = get_key_value(
#         key=constants.KEY_NAME_OPENAI_API_KEY,
#     )

#     print(f"OPENAI API Key: {api_key}")


# if __name__ == "__main__":
#     try:
#         main()

#     except KeyboardInterrupt:
#         print()

#     except Exception as exception:
#         print(f"[red][bold][-][/bold] {exception}![/red]")

#     finally:
#         print("=" * 50)
#         print()
# **************************************************

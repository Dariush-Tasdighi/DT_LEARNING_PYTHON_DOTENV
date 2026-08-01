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
# **************************************************


# **************************************************
# Display Version (Semi Best Practice)
# **************************************************
# from dotenv import version

# print()
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

# print()
# print("=" * 50)
# print(f"Version of 'dotenv' package: {version.__version__}")
# print("=" * 50)
# print()
# **************************************************


# **************************************************
# Display Version (Bad Practice)
#
# Check 'DT_Learning_Python_Advance' repository for more details!
# **************************************************
# import os
# from rich import print
# from dotenv import version

# os.system("cls")

# # print()
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
#     args="cls" if os.name == "nt" else "clear",
# )

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


# def clear_screen() -> None:
#     """
#     Clear screen
#     """

#     subprocess.run(
#         shell=True,
#         check=True,
#         capture_output=False,
#         args="cls" if os.name == "nt" else "clear",
#     )


# clear_screen()

# print("=" * 50)
# print(f"Version of 'dotenv' package: {version.__version__}")
# print("=" * 50)
# print()
# **************************************************


# **************************************************
# Display Version (Best Practice)
# **************************************************
# # NEW
# import dt_utility

# from rich import print
# from dotenv import version

# # NEW
# dt_utility.clear_screen()

# # NEW
# # print("=" * 50)
# dt_utility.display_main_divider()

# print(f"Version of 'dotenv' package: {version.__version__}")

# # NEW
# # print("=" * 50)
# dt_utility.display_main_divider()

# print()
# **************************************************


# **************************************************
# Display Version (Best Practice)
# **************************************************
# # NEW
# # import dt_utility
# from dt_utility import (
#     clear_screen,
#     display_main_divider,
# )

# from rich import print
# from dotenv import version

# # NEW
# clear_screen()
# # dt_utility.clear_screen()

# # NEW
# # dt_utility.display_main_divider()
# display_main_divider()

# print(f"Version of 'dotenv' package: {version.__version__}")

# # NEW
# # dt_utility.display_main_divider()
# display_main_divider()

# print()
# **************************************************


# **************************************************
# Display Version (Best Practice)
# **************************************************
# from rich import print
# from dt_utility import (
#     clear_screen,
#     display_main_divider,
# )
# from dotenv import version

# clear_screen()

# display_main_divider()
# print(f"Version of 'dotenv' package: {version.__version__}")
# display_main_divider()
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
# from dt_utility import (
#     clear_screen,
#     display_main_divider,
# )
# from dotenv import load_dotenv

# clear_screen()
# display_main_divider()

# # NEW: Very Important!
# load_dotenv()

# # NEW: os.environ.get
# password = os.environ.get("PASSWORD")
# print(f"Password: {password}")

# openai_api_key = os.environ.get("OPENAI_API_KEY")
# print(f"OPENAI API Key: {openai_api_key}")

# display_main_divider()
# print()
# **************************************************


# **************************************************
# Step (2)
# **************************************************
# import os

# from rich import print
# from dt_utility import (
#     clear_screen,
#     display_main_divider,
# )
# from dotenv import load_dotenv

# clear_screen()
# display_main_divider()

# # NEW: override=True
# # با تشکر از آقای مهندس امیر باقری
# load_dotenv(override=True)

# # NEW: str | None AND (key="PASSWORD")
# password: str | None = os.environ.get(key="PASSWORD")
# print(f"Password: {password}")

# openai_api_key: str | None = os.environ.get("OPENAI_API_KEY")
# print(f"OPENAI API Key: {openai_api_key}")

# display_main_divider()
# print()
# **************************************************


# **************************************************
# Step (3)
# **************************************************
# import os

# from rich import print
# from dt_utility import (
#     clear_screen,
#     display_main_divider,
# )
# from dotenv import load_dotenv

# # NEW
# from typing import Optional

# clear_screen()
# display_main_divider()

# load_dotenv(override=True)

# # NEW: str | None -> Optional[str]
# password: Optional[str] = os.environ.get(key="PASSWORD")
# print(f"Password: {password}")

# openai_api_key: Optional[str] = os.environ.get(key="OPENAI_API_KEY")
# print(f"OPENAI API Key: {openai_api_key}")
# display_main_divider()
# print()
# **************************************************


# **************************************************
# Step (4)
# **************************************************
# import os

# from rich import print
# from dt_utility import (
#     clear_screen,
#     display_main_divider,
# )
# from typing import Optional
# from dotenv import load_dotenv

# clear_screen()
# display_main_divider()

# load_dotenv(override=True)

# # NEW: os.environ.get() -> os.getenv()
# password: Optional[str] = os.getenv(key="PASSWORD")
# print(f"Password: {password}")

# openai_api_key: Optional[str] = os.getenv(key="OPENAI_API_KEY")
# print(f"OPENAI API Key: {openai_api_key}")

# display_main_divider()
# print()
# **************************************************


# **************************************************
# Step (5)
# **************************************************
# import os

# from rich import print
# from dt_utility import (
#     clear_screen,
#     display_main_divider,
# )
# from typing import Optional
# from dotenv import load_dotenv

# clear_screen()
# display_main_divider()

# # NEW: لوس بازی
# # ********************
# # dotenv_path_file -> dotenv_file_path
# # ********************
# # dotenv_file_path: str = ".envTemp"
# # dotenv_file_path: str = ".\.envTemp"
# # dotenv_file_path: str = ".\\.envTemp"
# # dotenv_file_path: str = r".\.envTemp"
# dotenv_file_path: str = "./.envTemp"  # Best Practice

# load_dotenv(
#     override=True,
#     # NEW
#     dotenv_path=dotenv_file_path,
# )

# password: Optional[str] = os.getenv(key="PASSWORD")
# print(f"Password: {password}")

# openai_api_key: Optional[str] = os.getenv(key="OPENAI_API_KEY")
# print(f"OPENAI API Key: {openai_api_key}")

# display_main_divider()
# print()
# **************************************************


# **************************************************
# Step (6)
# **************************************************
# import os

# from rich import print
# from dt_utility import (
#     clear_screen,
#     display_main_divider,
# )
# from typing import Optional
# from dotenv import load_dotenv

# # NEW
# import sys

# # NEW: Final
# from typing import Final

# # NEW
# KEY_NAME_OPENAI_API_KEY: str = "GOOGOOLI"  # None
# # KEY_NAME_OPENAI_API_KEY: str = "NEW_PASSWORD"  # Empty = "" = Null String

# # NEW: Final
# # KEY_NAME_OPENAI_API_KEY: Final[str] = "OPENAI_API_KEY"
# # KEY_NAME_OPENAI_API_KEY: Final[str] = "   OPENAI_api_KEY  ".strip().upper()
# # KEY_NAME_OPENAI_API_KEY: Final[str] = "  OPENAI_  api  _KEY  ".replace(" ", "").upper()

# clear_screen()
# display_main_divider()

# load_dotenv(override=True)

# # NEW: key=KEY_NAME_OPENAI_API_KEY
# api_key: Optional[str] = os.getenv(key=KEY_NAME_OPENAI_API_KEY)

# # NEW: Simple! not api_key -> Means:
# # api_key is not None and is not Empty (Null String = "")!
# if not api_key:
#     print(f"Error: The key '{KEY_NAME_OPENAI_API_KEY}' not found or is empty!")

#     # print(f"[-] The key '{KEY_NAME_OPENAI_API_KEY}' not found or is empty!")

#     # print(f"[red][bold][-][/bold] The key '{KEY_NAME_OPENAI_API_KEY}' not found or is empty![/red]")

#     display_main_divider()
#     print()

#     quit()
#     # exit()
#     # sys.exit(1)  # 0: Without Error - 1: With Error

# print(f"OPENAI API Key: {api_key}")
# display_main_divider()
# print()
# **************************************************


# **************************************************
# Step (7)
# **************************************************
# # NEW: First -> Import Module(s)
# import os
# import sys

# # NEW
# # from typing import Final, Optional

# # NEW
# # from typing import Final
# # from typing import Optional

# # NEW
# from typing import (
#     Final,
#     Optional,
# )

# from rich import print
# from dt_utility import (
#     clear_screen,
#     display_main_divider,
#     # NEW
#     display_error_message,
# )
# from dotenv import load_dotenv

# # NEW: Second -> Constant(s)
# KEY_NAME_OPENAI_API_KEY: Final[str] = "GOOGOOLI".replace(" ", "").upper()
# # KEY_NAME_OPENAI_API_KEY: Final[str] = "OPENAI_API_KEY".replace(" ", "").upper()


# # NEW: Third -> Function(s)
# # NEW: Define 'get_key_value()' function
# def get_key_value(key: str) -> str:
#     """
#     Get key value
#     Note: This is 'DocString' and it is better to use 'google' style!
#     """

#     load_dotenv(override=True)

#     value: Optional[str] = os.getenv(key=key)

#     if not value:
#         message: str = f"The key '{key}' not found or is empty!"
#         display_error_message(message=message)
#         display_main_divider()
#         print()
#         sys.exit(1)

#     return value


# clear_screen()
# display_main_divider()

# # NEW
# api_key: str = get_key_value(
#     key=KEY_NAME_OPENAI_API_KEY,
# )

# print(f"OPENAI API Key: {api_key}")

# display_main_divider()
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
# def main():
#     print("Hello, World!")


# if __name__ == "__main__":
#     main()
# **************************************************


# **************************************************
# def main() -> None:
#     """Main function"""

#     print("Hello, World!")


# if __name__ == "__main__":
#     main()
# **************************************************


# **************************************************
# سلیقه من
# **************************************************
# def main() -> None:
#     """
#     Main function
#     """

#     print("Hello, World!")


# if __name__ == "__main__":
#     main()
# **************************************************


# **************************************************
# from rich import print
# from dt_utility import (
#     clear_screen,
#     display_main_divider,
#     # NEW
#     display_divider,
#     display_error_message,
# )


# def main() -> None:
#     """
#     Main function
#     """

#     clear_screen()
#     display_main_divider()

#     age_str: str = input("How old are you? ")
#     age: int = int(age_str)
#     print(f"You are {age} years old.")


# if __name__ == "__main__":
#     try:
#         main()

#     except KeyboardInterrupt:
#         # pass
#         print()

#     except Exception as exception:
#         # NEW
#         display_divider()
#         display_error_message(message=str(exception))

#     finally:
#         display_main_divider()
#         print()
# **************************************************
# **************************************************
# **************************************************


# **************************************************
# Step (8)
# **************************************************
# import os

# from typing import (
#     Final,
#     Optional,
# )
# from rich import print
# from dt_utility import (
#     clear_screen,
#     display_main_divider,
#     display_error_message,
# )
# from dotenv import load_dotenv

# KEY_NAME_OPENAI_API_KEY: Final[str] = "GOOGOOLI".replace(" ", "").upper()
# # KEY_NAME_OPENAI_API_KEY: Final[str] = "OPENAI_API_KEY".replace(" ", "").upper()


# def get_key_value(key: str) -> str:
#     """
#     Get key value
#     """

#     load_dotenv(override=True)

#     value: Optional[str] = os.getenv(key=key)

#     if not value:
#         # NEW
#         message: str = f"The key '{key}' not found or is empty"  # Remove '!'
#         raise Exception(message)

#     return value


# def main() -> None:
#     """
#     Main function
#     """

#     clear_screen()
#     display_main_divider()

#     api_key: str = get_key_value(
#         key=KEY_NAME_OPENAI_API_KEY,
#     )

#     print(f"OPENAI API Key: {api_key}")


# if __name__ == "__main__":
#     try:
#         main()

#     except KeyboardInterrupt:
#         print()

#     except Exception as exception:
#         display_error_message(message=str(exception))

#     finally:
#         display_main_divider()
#         print()
# **************************************************


# **************************************************
# Step (9)
# **************************************************
# """
# Some Description
# """

# # NEW
# import app_constants as constants

# from rich import print
# from dt_utility import (
#     clear_screen,
#     display_main_divider,
#     display_error_message,
# )

# # NEW
# from dt_dotenv import get_key_value


# def main() -> None:
#     """
#     Main function
#     """

#     clear_screen()
#     display_main_divider()

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
#         display_error_message(message=str(exception))

#     finally:
#         display_main_divider()
#         print()
# **************************************************

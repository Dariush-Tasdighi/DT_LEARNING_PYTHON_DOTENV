# **************************************************
# روش احمقانه
# **************************************************
from openai import OpenAI

OPENAI_API_KEY: str = "abcde...12345"

client = OpenAI(api_key=OPENAI_API_KEY)
# **************************************************


# **************************************************
# Display Version
# **************************************************
# from dotenv import version

# print(f"Version of 'dotenv': {version.__version__}")
# **************************************************


# **************************************************
# ‌Bad Practice
# **************************************************
# import os
# from dotenv import load_dotenv

# load_dotenv()

# password = os.environ.get("PASSWORD")
# print(f"Password: {password}")

# openai_api_key = os.environ.get("OPENAI_API_KEY")
# print(f"OPENAI API Key: {openai_api_key}")
# **************************************************


# **************************************************
# Solution (1)
# **************************************************
# import os
# from dotenv import load_dotenv

# # NEW
# # os.system("cls")

# # NEW
# # os.system(command="cls")

# # NEW
# # if os.name == "nt":
# #     os.system(command="cls")
# # else:
# #     os.system(command="clear")

# # NEW
# os.system(command="cls" if os.name == "nt" else "clear")

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
# **************************************************


# **************************************************
# Solution (2)
# **************************************************
# import os
# from dotenv import load_dotenv

# os.system(command="cls" if os.name == "nt" else "clear")

# load_dotenv(override=True)

# # NEW: os.getenv
# password: str | None = os.getenv(key="PASSWORD")
# print(f"Password: {password}")

# openai_api_key: str | None = os.getenv(key="OPENAI_API_KEY")
# print(f"OPENAI API Key: {openai_api_key}")
# **************************************************


# **************************************************
# Solution (3)
# **************************************************
# import os
# from dotenv import load_dotenv

# os.system(command="cls" if os.name == "nt" else "clear")

# load_dotenv(
#     override=True,
#     # NEW: لوس‌بازی
#     dotenv_path="./.envTemp",
# )

# password: str | None = os.getenv(key="PASSWORD")
# print(f"Password: {password}")

# openai_api_key: str | None = os.getenv(key="OPENAI_API_KEY")
# print(f"OPENAI API Key: {openai_api_key}")
# **************************************************


# **************************************************
# Best Practice (1)
# **************************************************
# import os
# from dotenv import load_dotenv

# # NEW
# # KEY_NAME_OPENAI_API_KEY: str = "GOOGOOLI"
# # KEY_NAME_OPENAI_API_KEY: str = "NEW_PASSWORD"
# KEY_NAME_OPENAI_API_KEY: str = "OPENAI_API_KEY"

# os.system(command="cls" if os.name == "nt" else "clear")

# load_dotenv(override=True)

# # NEW
# api_key: str | None = os.getenv(
#     key=KEY_NAME_OPENAI_API_KEY,
# )

# # NEW
# if not api_key:
#     print(f"[-] Key '{KEY_NAME_OPENAI_API_KEY}' not found or is empty!")
#     exit()

# print(f"OPENAI API Key: {api_key}")
# **************************************************


# **************************************************
# Best Practice (2)
# **************************************************
# import os
# from dotenv import load_dotenv

# # KEY_NAME_OPENAI_API_KEY: str = "GOOGOOLI"
# # KEY_NAME_OPENAI_API_KEY: str = "NEW_PASSWORD"
# KEY_NAME_OPENAI_API_KEY: str = "OPENAI_API_KEY"


# # NEW
# def get_key_value(key: str) -> str:
#     """Get key value."""

#     load_dotenv(override=True)

#     value: str | None = os.getenv(key=key)

#     if not value:
#         # NEW: \n
#         print(f"[-] Key '{key}' not found or is empty!\n")
#         exit()

#     return value


# os.system(command="cls" if os.name == "nt" else "clear")

# # NEW
# api_key: str = get_key_value(
#     key=KEY_NAME_OPENAI_API_KEY,
# )

# print(f"OPENAI API Key: {api_key}")
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
#     """Main of program."""

#     print("Hello, World!")


# if __name__ == "__main__":
#     main()
# **************************************************


# **************************************************
# Best Practice (3)
# **************************************************
# import os
# from dotenv import load_dotenv

# # KEY_NAME_OPENAI_API_KEY: str = "GOOGOOLI"
# # KEY_NAME_OPENAI_API_KEY: str = "NEW_PASSWORD"
# KEY_NAME_OPENAI_API_KEY: str = "OPENAI_API_KEY"


# def get_key_value(key: str) -> str:
#     """Get key value."""

#     load_dotenv(override=True)

#     value: str | None = os.getenv(key=key)

#     if not value:
#         print(f"[-] Key '{key}' not found or is empty!\n")
#         exit()

#     return value


# # NEW
# def main() -> None:
#     """Main of program."""

#     os.system(command="cls" if os.name == "nt" else "clear")

#     api_key: str = get_key_value(
#         key=KEY_NAME_OPENAI_API_KEY,
#     )

#     print(f"OPENAI API Key: {api_key}")


# # NEW
# if __name__ == "__main__":
#     main()
# **************************************************


# **************************************************
# Best Practice (4)
# **************************************************
# """
# Sample code for using 'dotenv' package.
# """

# import os

# # NEW
# import dt_dotenv as utility
# import app_constants as constants


# def main() -> None:
#     """Main of program."""

#     os.system(command="cls" if os.name == "nt" else "clear")

#     # NEW
#     api_key: str = utility.get_key_value(
#         key=constants.KEY_NAME_OPENAI_API_KEY,
#     )

#     print(f"OPENAI API Key: {api_key}")


# if __name__ == "__main__":
#     main()
# **************************************************

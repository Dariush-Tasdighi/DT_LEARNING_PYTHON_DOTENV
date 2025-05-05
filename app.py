# **************************************************
# روش احمقانه
# **************************************************
from openai import OpenAI

OPENAI_API_KEY: str = "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"

client = OpenAI(api_key=OPENAI_API_KEY)
# **************************************************


# **************************************************
# Solution (1)
# **************************************************
# import os
# from dotenv import load_dotenv

# os.system(command="cls")

# load_dotenv(override=True)

# password = os.getenv(key="PASSWORD")
# print("Password:", password)

# openai_api_key = os.getenv(key="OPENAI_API_KEY")
# print("OPENAI API Key:", openai_api_key)
# **************************************************


# **************************************************
# Solution (2)
# **************************************************
# import os
# from dotenv import load_dotenv

# os.system(command="cls")

# load_dotenv(override=True)

# password = os.environ.get(key="PASSWORD")
# print("Password:", password)

# openai_api_key = os.environ.get(key="OPENAI_API_KEY")
# print("OPENAI API Key:", openai_api_key)
# **************************************************


# **************************************************
# Solution (3)
# **************************************************
# import os
# from dotenv import load_dotenv

# os.system(command="cls")

# load_dotenv(
#     override=True,
#     dotenv_path="./.envTemp",
# )

# password = os.getenv(key="PASSWORD")
# print("Password:", password)

# openai_api_key = os.getenv(key="OPENAI_API_KEY")
# print("OPENAI API Key:", openai_api_key)
# **************************************************


# **************************************************
# Best Practice (1)
# **************************************************
# import os
# from dotenv import load_dotenv

# # KEY_NAME_OPENAI_API_KEY: str = "GOOGOOLI"
# KEY_NAME_OPENAI_API_KEY: str = "OPENAI_API_KEY"

# os.system(command="cls")

# load_dotenv(override=True)

# api_key: str | None = os.getenv(key=KEY_NAME_OPENAI_API_KEY)

# if api_key is None:
#     print(f"[-] API Key '{KEY_NAME_OPENAI_API_KEY}' not found!")
#     exit()

# print("OPENAI API Key:", api_key)
# **************************************************


# **************************************************
# Best Practice (2)
# **************************************************
# import os
# from dotenv import load_dotenv

# KEY_NAME_OPENAI_API_KEY: str = "OPENAI_API_KEY"


# def get_api_key(key: str) -> str:
#     """
#     Get API key.
#     """

#     load_dotenv(override=True)

#     api_key: str | None = os.getenv(key=key)

#     if not api_key:
#         print(f"[-] API Key '{key}' not found!")
#         exit()

#     return api_key


# os.system(command="cls")

# api_key: str = get_api_key(key=KEY_NAME_OPENAI_API_KEY)

# print("OPENAI API Key:", api_key)
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
#     Main Function
#     """

#     print("Hello, World!")


# if __name__ == "__main__":
#     main()
# **************************************************


# **************************************************
# Best Practice (3)
# **************************************************
# import os
# from dotenv import load_dotenv

# KEY_NAME_OPENAI_API_KEY: str = "OPENAI_API_KEY"


# def get_api_key(key: str) -> str:
#     """
#     Get API key.
#     """

#     load_dotenv(override=True)

#     api_key: str | None = os.getenv(key=key)

#     if not api_key:
#         print(f"[-] API Key '{key}' not found!")
#         exit()

#     return api_key


# def main() -> None:
#     """
#     Main Function
#     """

#     os.system(command="cls")

#     api_key: str = get_api_key(key=KEY_NAME_OPENAI_API_KEY)

#     print("OPENAI API Key:", api_key)


# if __name__ == "__main__":
#     main()
# **************************************************


# **************************************************
# Best Practice (4)
# **************************************************
# """
# Start of the Code
# """

# import os
# import app_constants as constants
# import app_functions as functions


# def main() -> None:
#     """
#     Main Function
#     """

#     os.system(command="cls")

#     api_key: str = functions.get_api_key(
#         key=constants.KEY_NAME_OPENAI_API_KEY,
#     )

#     print("API Key:", api_key)
#     print("OPENAI API Key:", api_key)


# if __name__ == "__main__":
#     main()
# **************************************************

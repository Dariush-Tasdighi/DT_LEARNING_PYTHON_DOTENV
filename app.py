# **************************************************
# روش احمقانه
# **************************************************
from openai import OpenAI

api_key = "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"

client = OpenAI(api_key=api_key)
# **************************************************


# **************************************************
# Solution (1)
# **************************************************
# import os
# from dotenv import load_dotenv

# os.system(command="cls")

# load_dotenv()

# password = os.getenv(key="PASSWORD")
# print("Password:", password)

# api_key = os.getenv(key="OPENAI_API_KEY")
# print("API Key:", api_key)
# **************************************************


# **************************************************
# Solution (2)
# **************************************************
# import os
# from dotenv import load_dotenv

# os.system(command="cls")

# load_dotenv()

# password = os.environ.get(key="PASSWORD")
# print("Password:", password)

# api_key = os.environ.get(key="OPENAI_API_KEY")
# print("API Key:", api_key)
# **************************************************


# **************************************************
# Solution (3)
# **************************************************
# import os
# from dotenv import load_dotenv

# os.system(command="cls")

# load_dotenv(dotenv_path="./.envTemp")

# password = os.environ.get(key="PASSWORD")
# print("Password:", password)

# api_key = os.environ.get(key="OPENAI_API_KEY")
# print("API Key:", api_key)
# **************************************************


# **************************************************
# Best Practice (1)
# **************************************************
# import os
# from dotenv import load_dotenv

# os.system(command="cls")

# load_dotenv()

# # KEY_NAME_API_KEY: str = "GOOGOOLI"
# KEY_NAME_API_KEY: str = "OPENAI_API_KEY"

# api_key: str | None = os.getenv(key=KEY_NAME_API_KEY)

# if api_key is None:
#     print("[-] API Key not found!")
#     exit()

# print("API Key:", api_key)
# **************************************************


# **************************************************
# Best Practice (2)
# **************************************************
# import os
# from dotenv import load_dotenv

# KEY_NAME_API_KEY: str = "OPENAI_API_KEY"


# def get_api_key() -> str:
#     """
#     Get API Key Function
#     """

#     load_dotenv()

#     api_key: str | None = os.getenv(key=KEY_NAME_API_KEY)
#     if not api_key:
#         print("API Key not found!")
#         exit()

#     return api_key


# os.system(command="cls")

# api_key: str = get_api_key()

# print("API Key:", api_key)
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

# KEY_NAME_API_KEY: str = "OPENAI_API_KEY"


# def get_api_key() -> str:
#     """
#     Get API Key Function
#     """

#     load_dotenv()

#     api_key: str | None = os.getenv(key=KEY_NAME_API_KEY)
#     if not api_key:
#         print("API Key not found!")
#         exit()

#     return api_key


# def main() -> None:
#     """
#     Main Function
#     """

#     os.system(command="cls")

#     api_key: str = get_api_key()

#     print("API Key:", api_key)


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
# import app_functions as functions


# def main() -> None:
#     """
#     Main Function
#     """

#     os.system(command="cls")

#     api_key: str = functions.get_api_key()

#     print("API Key:", api_key)


# if __name__ == "__main__":
#     main()
# **************************************************

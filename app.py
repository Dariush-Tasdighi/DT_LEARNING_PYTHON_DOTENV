"""
Sample code for using 'dotenv' package.
"""

import os

# NEW
import dt_llm_utility as utility
import app_constants as constants


def main() -> None:
    """
    Main function.
    """

    os.system(command="cls" if os.name == "nt" else "clear")

    # NEW
    api_key: str = utility.get_key_value(
        key=constants.KEY_NAME_OPENAI_API_KEY,
    )

    print(f"OPENAI API Key: {api_key}")


if __name__ == "__main__":
    main()

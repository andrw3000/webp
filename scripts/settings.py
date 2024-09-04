from typing import Optional

from dotenv import find_dotenv
from pydantic import ConfigDict
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Read environment variables from the .env file and validate them.
    """

    twinlab_api_key: str
    my_optional_secret: Optional[str] = None

    model_config = ConfigDict(
        env_file=find_dotenv(), extra="ignore", env_file_encoding="utf-8"
    )


try:
    SETTINGS = Settings()
except Exception as err:
    print(f"Error reading settings: {err}.")
    exit(1)


if __name__ == "__main__":
    print("My twinLab API key is...")
    print(f"{SETTINGS.twinlab_api_key}\n")

    if SETTINGS.my_optional_secret:
        print("I'm going to tell you an optional secret...")
        print(f"{SETTINGS.my_optional_secret}")

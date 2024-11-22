import os
from typing import Optional

from dotenv import load_dotenv


class Settings:
    def __init__(self):
        load_dotenv()
        self.token_bot: Optional[str] = os.getenv('token_bot')
        self.api_key: Optional[str] = os.getenv('api_key')
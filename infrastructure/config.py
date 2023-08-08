import os.path
from typing import Optional

from pydantic import BaseSettings


class Config(BaseSettings):
    MONGODB_URL: str
    APP_ENV: Optional[str] = 'dev'

    class Config:
        env_file = os.path.join(os.path.dirname(__file__), '../.env')
        env_file_encoding = 'utf-8'


config = Config()

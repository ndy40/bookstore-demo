import os.path
from typing import Optional

from pydantic import BaseSettings, Field


class Config(BaseSettings):
    MONGODB_URL: str
    DB_NAME: Optional[str] = 'bookstore'
    APP_ENV: Optional[str] = Field(env='APP_ENV', default='dev')

    class Config:
        env_file = os.path.join(os.path.dirname(__file__), '../.env')
        env_file_encoding = 'utf-8'

    @property
    def db_name(self):
        if self.APP_ENV == 'test':
            return 'bookstore_tests'
        return self.DB_NAME


config = Config()  # type: ignore

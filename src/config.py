"""
See:
- https://fastapi.tiangolo.com/advanced/settings/
- https://pydantic-docs.helpmanual.io/usage/settings/
"""

import os

from pydantic import BaseSettings


class Settings(BaseSettings):
    database_url: str
    aws_access_key: str
    aws_secret: str
    sns_topic_arn: str

    class Config:
        env_file = ".env"


class ProdSettings(Settings):
    database_url: str

    class Config:
        env_prefix = "PROD_"


class DevSettings(Settings):
    # Environment variables will take priority, so DATABASE_URL is overridden
    # when running on Docker because `localhost` cannot be used
    database_url = "mysql+pymysql://dbuser:dbuser@localhost:3306/dnyf-group-db"


if os.getenv("PROD_FLAG"):
    settings = ProdSettings()
else:
    settings = DevSettings()

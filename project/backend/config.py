import os

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=os.environ.get("ENV_FILE", ".env"),
        arbitrary_types_allowed=True,
        extra="allow",
    )

    SECRET_KEY: str


settings = Settings()

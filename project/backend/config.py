import os

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # This is Pydantic model config, not to be confused with AI model config
    model_config = SettingsConfigDict(
        env_file=os.environ.get("ENV_FILE", ".env"),
        arbitrary_types_allowed=True,
        extra="allow",
    )

    SECRET_KEY: str


settings = Settings()

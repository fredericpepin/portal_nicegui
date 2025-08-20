from pydantic_settings import BaseSettings

__all__ = [
    "app_settings",
    ]

class Settings(BaseSettings):
    app_title: str = "D&G Portal"

    class Config:
        env_prefix = "NICEGUI_"

app_settings = Settings()
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_host: str = "0.0.0.0",
    app_port: int = 8000
    telegram_bot_token: str
    telegram_chat_id: str

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
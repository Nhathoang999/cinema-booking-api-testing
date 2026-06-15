from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    jwt_secret_key: str = "fallback_secret_key_for_dev_only"
    access_token_expire_minutes: int = 30
    database_url: str = "sqlite:///./cinema.db"

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()

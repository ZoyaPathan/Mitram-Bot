from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "MITRAM Bot Backend"
    app_version: str = "1.0.0"

    bot_id: str = "MITRAM-001"
    environment: str = "development"
    backend_url: str = "http://localhost:8000"

    database_url: str = "sqlite:///./mitram.db"
    log_level: str = "INFO"

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )


settings = Settings()
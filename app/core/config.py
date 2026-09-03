from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict


class Settings(BaseSettings):
    database_url: str = (
        "postgresql+psycopg://postgres:password@127.0.0.1:5432/job_resume_matcher"
    )

    secret_key: str = "change-this-secret-key"

    algorithm: str = "HS256"

    access_token_expire_minutes: int = 30

    openrouter_api_key: str | None = None

    openrouter_base_url: str = (
        "https://openrouter.ai/api/v1"
    )

    llm_model: str = "your-model-name"

    llm_timeout_seconds: int = 60

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )


settings = Settings()
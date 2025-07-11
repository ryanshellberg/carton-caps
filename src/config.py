from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=(".env.local"), env_file_encoding="utf-8", extra="ignore"
    )

    openai_api_key: str
    openai_embedding_model: str = "text-embedding-3-large"
    openai_chat_model: str = "gpt-4o"
    openai_temperature: float = 0.2


settings = Settings()

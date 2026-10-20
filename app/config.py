"""Application configuration loaded from environment variables and .env."""

from collections.abc import Mapping

from pydantic import model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Settings required to run the ticket triage application."""

    llm_api_key: str
    llm_model: str
    database_url: str

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    @model_validator(mode="before")
    @classmethod
    def require_llm_api_key(cls, values: object) -> object:
        if isinstance(values, Mapping) and not values.get("llm_api_key"):
            raise ValueError("LLM_API_KEY is required; set it in the .env file.")
        return values

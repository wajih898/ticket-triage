"""Tests for application configuration."""

from pathlib import Path

import pytest
from pydantic import ValidationError

from app.config import Settings


def test_settings_load_values_from_dotenv(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.chdir(tmp_path)
    monkeypatch.delenv("LLM_API_KEY", raising=False)
    monkeypatch.delenv("LLM_MODEL", raising=False)
    monkeypatch.delenv("DATABASE_URL", raising=False)
    (tmp_path / ".env").write_text(
        "LLM_API_KEY=test-key\nLLM_MODEL=test-model\nDATABASE_URL=sqlite:///test.db\n",
        encoding="utf-8",
    )

    settings = Settings()

    assert settings.llm_api_key == "test-key"
    assert settings.llm_model == "test-model"
    assert settings.database_url == "sqlite:///test.db"


def test_settings_require_llm_api_key(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("LLM_API_KEY", raising=False)
    with pytest.raises(ValidationError, match="LLM_API_KEY is required"):
        Settings(_env_file=None, llm_model="test-model", database_url="sqlite:///test.db")

# backend/app/core/config.py
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    LLM_API_KEY: str
    LLM_BASE_URL: str
    LLM_MODEL: str

    # 从项目根目录加载 .env，相对路径是相对于当前执行入口main.py
    model_config = SettingsConfigDict(
        env_file="../../.env",
        env_file_encoding="utf-8"
    )

settings = Settings()

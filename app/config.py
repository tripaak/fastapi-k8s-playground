from pydantic_settings import BaseSettings
from functools import lru_cache
from typing import List

class Settings(BaseSettings):
    APP_NAME: str = "fastapi-k8s-app"
    VERSION: str = "1.0.0"
    ENVIRONMENT: str = "development"  # development|staging|production

    API_V1_PREFIX: str = "/api/v1"
    ENABLE_DOCS: bool = True

    # DB
    DATABASE_URL: str  # Example: postgresql+asyncpg://user:pass@postgres:5432/appdb
    DB_POOL_SIZE: int = 10
    DB_MAX_OVERFLOW: int = 20

    # CORS
    ALLOWED_ORIGINS: List[str] = ["*"]
    ALLOWED_METHODS: List[str] = ["*"]
    ALLOWED_HEADERS: List[str] = ["*"]

    # Logging
    LOG_LEVEL: str = "INFO"
    LOG_FORMAT: str = "json"  # json|text

    class Config:
        env_file = ".env"
        case_sensitive = True

# @lru_cache: A decorator that caches the function's return value. The first time get_settings() is called, 
# it creates a Settings object and stores it. 
# Every subsequent call returns the cached object instead of creating a new one.
@lru_cache
def get_settings() -> Settings:
    return Settings()
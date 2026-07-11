from typing import List, Optional
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field
import os
import logging

logger = logging.getLogger(__name__)

class Settings(BaseSettings):
    """
    Application configuration via environment variables.
    """
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

    # Application
    APP_ENV: str = Field(default="development")
    LOG_LEVEL: str = Field(default="INFO")
    LOG_FILE: str = Field(default="/tmp/nursing_validator.log")

    # Security / Users
    # Optional bootstrap credentials. No credentials are supplied by the
    # application. Production deployments must use a database/identity
    # provider and explicitly configure any one-time bootstrap accounts.
    ADMIN_PASSWORD: Optional[str] = Field(default=None)
    NURSE_PASSWORD: Optional[str] = Field(default=None)
    CLINICIAN_PASSWORD: Optional[str] = Field(default=None)
    ALLOW_IN_MEMORY_AUTH: bool = Field(default=False)

    # Database
    USE_DATABASE: bool = Field(default=True)
    DB_TYPE: str = Field(default="sqlite")  # postgres or sqlite
    SQLITE_DB_PATH: str = Field(default="nursing_validator.db")
    
    # Postgres Settings
    DB_HOST: str = Field(default="localhost")
    DB_PORT: str = Field(default="5432")
    DB_NAME: str = Field(default="nursing_validator")
    DB_USER: str = Field(default="nursing_admin")
    DB_PASSWORD: Optional[str] = Field(default=None)
    DB_POOL_MIN: int = Field(default=2)
    DB_POOL_MAX: int = Field(default=20)

    # Vector Database
    VECTOR_DB_PATH: str = Field(default="chroma_db_fons")
    LOCAL_DB_PATH: str = Field(default="/tmp/chroma_db_fons_fast")
    EMBEDDING_MODEL: str = Field(default="text-embedding-ada-002")

    # Azure OpenAI
    AZURE_OPENAI_ENDPOINT: Optional[str] = Field(default=None)
    AZURE_OPENAI_API_KEY: Optional[str] = Field(default=None)
    AZURE_OPENAI_API_VERSION: Optional[str] = Field(default="2023-05-15")
    AZURE_OPENAI_DEPLOYMENT: Optional[str] = Field(default=None)

    # Streamlit Specific
    STREAMLIT_SERVER_HEADLESS: bool = Field(default=True)
    STREAMLIT_SERVER_ENABLE_CORS: bool = Field(default=False)

    def is_production(self) -> bool:
        return self.APP_ENV.lower() == "production"

    def check_security(self):
        """Reject insecure production configuration and warn in development."""
        configured = [
            self.ADMIN_PASSWORD,
            self.NURSE_PASSWORD,
            self.CLINICIAN_PASSWORD,
        ]
        placeholders = {
            "change_me_admin", "change_me_nurse", "change_me_clinician",
            "change_me_admin_secure", "change_me_nurse_secure",
            "change_me_clinician_secure", "admin" + "2025", "nurse" + "2025",
            "clinician" + "2025",
        }
        insecure = any(value in placeholders for value in configured if value)
        if self.is_production():
            if self.ALLOW_IN_MEMORY_AUTH:
                raise ValueError("ALLOW_IN_MEMORY_AUTH must be false in production")
            if insecure:
                raise ValueError("Placeholder user credentials are forbidden in production")
            if self.DB_TYPE == "postgres" and not self.DB_PASSWORD:
                raise ValueError("DB_PASSWORD is required for production PostgreSQL")
        elif insecure:
            logger.warning("Placeholder credentials detected; do not use this configuration clinically")

# Create a global instance
settings = Settings()
settings.check_security()

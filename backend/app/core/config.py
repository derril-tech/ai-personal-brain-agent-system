"""
MindMesh Configuration Management
"""

import os
from typing import List, Optional
from pydantic import Field, validator
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings"""
    
    # Application
    APP_NAME: str = "MindMesh"
    APP_VERSION: str = "1.0.0"
    ENVIRONMENT: str = "development"
    DEBUG: bool = True
    LOG_LEVEL: str = "INFO"
    
    # Database
    DATABASE_URL: str = Field(
        default="postgresql+asyncpg://mindmesh_user:mindmesh_password@localhost:5432/mindmesh",
        description="Database connection URL"
    )
    DATABASE_POOL_SIZE: int = 20
    DATABASE_MAX_OVERFLOW: int = 30
    DATABASE_POOL_TIMEOUT: int = 30
    
    # Redis
    REDIS_URL: str = "redis://localhost:6379/0"
    REDIS_PASSWORD: Optional[str] = None
    REDIS_DB: int = 0
    REDIS_POOL_SIZE: int = 10
    
    # JWT
    JWT_SECRET_KEY: str = Field(..., description="JWT secret key")
    JWT_ALGORITHM: str = "HS256"
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    JWT_REFRESH_TOKEN_EXPIRE_DAYS: int = 7
    
    # AI/ML
    OPENAI_API_KEY: Optional[str] = None
    OPENAI_MODEL: str = "gpt-4-turbo-preview"
    OPENAI_MAX_TOKENS: int = 4000
    OPENAI_TEMPERATURE: float = 0.1
    
    ANTHROPIC_API_KEY: Optional[str] = None
    ANTHROPIC_MODEL: str = "claude-3-sonnet-20240229"
    
    LANGSMITH_API_KEY: Optional[str] = None
    LANGSMITH_ENDPOINT: str = "http://localhost:1984"
    LANGSMITH_PROJECT: str = "mindmesh-dev"
    
    VECTOR_DIMENSION: int = 1536
    VECTOR_SIMILARITY_METRIC: str = "cosine"
    
    # Storage
    S3_ENDPOINT_URL: str = "http://localhost:9000"
    S3_ACCESS_KEY_ID: str = "minioadmin"
    S3_SECRET_ACCESS_KEY: str = "minioadmin123"
    S3_BUCKET_NAME: str = "mindmesh-storage"
    S3_REGION: str = "us-east-1"
    
    # Connectors
    GMAIL_CLIENT_ID: Optional[str] = None
    GMAIL_CLIENT_SECRET: Optional[str] = None
    GMAIL_REDIRECT_URI: str = "http://localhost:3000/api/auth/gmail/callback"
    
    GOOGLE_CALENDAR_CLIENT_ID: Optional[str] = None
    GOOGLE_CALENDAR_CLIENT_SECRET: Optional[str] = None
    GOOGLE_CALENDAR_REDIRECT_URI: str = "http://localhost:3000/api/auth/google-calendar/callback"
    
    GOOGLE_DRIVE_CLIENT_ID: Optional[str] = None
    GOOGLE_DRIVE_CLIENT_SECRET: Optional[str] = None
    GOOGLE_DRIVE_REDIRECT_URI: str = "http://localhost:3000/api/auth/google-drive/callback"
    
    SLACK_CLIENT_ID: Optional[str] = None
    SLACK_CLIENT_SECRET: Optional[str] = None
    SLACK_REDIRECT_URI: str = "http://localhost:3000/api/auth/slack/callback"
    
    NOTION_CLIENT_ID: Optional[str] = None
    NOTION_CLIENT_SECRET: Optional[str] = None
    NOTION_REDIRECT_URI: str = "http://localhost:3000/api/auth/notion/callback"
    
    # Security & Privacy
    ENCRYPTION_KEY: str = Field(..., description="32-byte encryption key")
    PII_REDACTION_ENABLED: bool = True
    AUDIT_LOG_ENABLED: bool = True
    DATA_RETENTION_DAYS: int = 365
    
    # Performance & Monitoring
    MAX_CONCURRENT_RUNS: int = 10
    RUN_TIMEOUT_SECONDS: int = 300
    COST_BUDGET_PER_GOAL: float = 5.00
    TELEMETRY_ENABLED: bool = True
    
    # CORS
    ALLOWED_HOSTS: List[str] = ["http://localhost:3000", "http://127.0.0.1:3000"]
    
    @validator("ALLOWED_HOSTS", pre=True)
    def assemble_cors_origins(cls, v):
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)
    
    class Config:
        env_file = ".env"
        case_sensitive = True


# Global settings instance
settings = Settings()

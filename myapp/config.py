from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DB_REGION_NAME: str
    DB_ACCESS_KEY_ID: str
    DB_SECRET_ACCESS_KEY: str
    ENVIRONMENT: str = "production"

    class Config:
        env_file = ".env"

settings = Settings()
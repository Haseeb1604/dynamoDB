from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_HOSTNAME: str

    class Config:
        env_file = ".env"

settings = Settings()
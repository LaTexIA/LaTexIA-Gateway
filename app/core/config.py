import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    API_VERSION: str = "v1"
    PREPROCESSING_URL: str = os.getenv("PREPROCESSING_URL", "http://localhost:8001")
    LATEX_RECOGNITION_URL: str = os.getenv("LATEX_RECOGNITION_URL", "http://localhost:8003")

    class Config:
        env_file = ".env"

settings = Settings()
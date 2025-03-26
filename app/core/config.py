import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    API_VERSION: str = "v1"
    PREPROCESSING_URL: str = os.getenv("PREPROCESSING_URL", "http://preprocessing-service:8001")
    LATEX_RECOGNITION_URL: str = os.getenv("LATEX_RECOGNITION_URL", "http://latex-recognition-service:8003")

    class Config:
        env_file = ".env"

settings = Settings()
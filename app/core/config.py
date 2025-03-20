import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    API_VERSION: str = "v1"
    AUTH_SERVICE_URL: str = os.getenv("AUTH_SERVICE_URL", "http://auth-service:8001")
    TEXT_RECOGNITION_URL: str = os.getenv("TEXT_RECOGNITION_URL", "http://text-recognition-service:8002")
    LATEX_RECOGNITION_URL: str = os.getenv("LATEX_RECOGNITION_URL", "http://latex-recognition-service:8003")
    EVALUATION_SERVICE_URL: str = os.getenv("EVALUATION_SERVICE_URL", "http://evaluation-service:8004")

    class Config:
        env_file = ".env"

settings = Settings()
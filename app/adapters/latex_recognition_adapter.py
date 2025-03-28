import httpx
from app.core.config import settings

class LatexRecognitionAdapter:
    def __init__(self, api_url: str):
        self.api_url = api_url
        self.client = httpx.AsyncClient(follow_redirects=True)

    async def recognize_formula(self, image_data: bytes):
        """Envía la imagen al servicio de reconocimiento de LaTeX y devuelve el código LaTeX"""
        response = await self.client.post(f"{self.api_url}/predict/", files={"file": image_data})
        return response.json()["predicted_class"]
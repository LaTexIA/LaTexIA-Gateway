import httpx
from app.core.config import settings

async def recognize_formula(image: bytes):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{settings.LATEX_RECOGNITION_URL}/predict", 
            files={"file": image}
        )
        return response.json()

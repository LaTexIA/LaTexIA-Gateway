import requests
from io import BytesIO
from app.ports.preprocessing_port import PreprocessingPort

class PreprocessingAdapter(PreprocessingPort):
    def __init__(self, api_url: str):
        self.api_url = api_url

    async def send_image(self, image_data: BytesIO):
        """ Envía la imagen al microservicio de preprocesamiento y recibe la respuesta """
        files = {"file": ("image.jpg", image_data.getvalue(), "image/jpeg")}
        
        response = requests.post(f"{self.api_url}/preprocess/", files=files)
        response.raise_for_status()  # Verificar que la petición fue exitosa
        
        return response.json()  # Devolvemos la imagen procesada
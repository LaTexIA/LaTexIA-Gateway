from io import BytesIO
from app.ports.preprocessing_port import PreprocessingPort

class PreprocessingService:
    def __init__(self, preprocessing_port: PreprocessingPort):
        self.preprocessing_port = preprocessing_port

    async def preprocess_image(self, image_data: BytesIO):
        """ Llama al adaptador para enviar la imagen al servicio """
        return await self.preprocessing_port.send_image(image_data)

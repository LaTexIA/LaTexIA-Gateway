from abc import ABC, abstractmethod
from io import BytesIO

class PreprocessingPort(ABC):
    @abstractmethod
    async def send_image(self, image_data: BytesIO):
        """ Enviar la imagen al servicio de preprocesamiento """
        pass

from app.ports.latex_recognition_port import LatexRecognitionPort

class LatexRecognitionService:
    def __init__(self, latex_recognition_port: LatexRecognitionPort):
        self.latex_recognition_port = latex_recognition_port

    async def recognize_formula(self, image_data: bytes):
        """Llama al adaptador para enviar la imagen al servicio de reconocimiento de LaTeX"""
        return await self.latex_recognition_port.recognize_formula(image_data)
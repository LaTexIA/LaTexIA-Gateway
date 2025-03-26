from fastapi import APIRouter, File, UploadFile, Depends
from app.adapters.latex_recognition_adapter import LatexRecognitionAdapter
from app.core.latex_recognition_service import LatexRecognitionService
from app.core.config import settings

router = APIRouter()

# Configuración del adaptador y servicio
latex_recognition_adapter = LatexRecognitionAdapter(api_url=settings.LATEX_RECOGNITION_URL)
latex_recognition_service = LatexRecognitionService(latex_recognition_port=latex_recognition_adapter)

@router.post("/predict/")
async def predict(file: UploadFile = File(...)):
    """Recibe una imagen preprocesada y devuelve el código LaTeX"""
    image_data = await file.read()  # Lee los bytes de la imagen
    latex_code = await latex_recognition_service.recognize_formula(image_data)
    return {"latex_code": latex_code}

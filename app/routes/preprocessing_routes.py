from fastapi import APIRouter, File, UploadFile
from io import BytesIO
from fastapi.responses import StreamingResponse
from app.adapters.preprocessing_adapter import PreprocessingAdapter
from app.core.preprocessing_service import PreprocessingService

from app.core.config import settings

router = APIRouter()

# Configuración del adaptador y servicio
preprocessing_adapter = PreprocessingAdapter(api_url=settings.PREPROCESSING_URL)
preprocessing_service = PreprocessingService(preprocessing_port=preprocessing_adapter)

@router.post("/process-image/")
async def process_image(file: UploadFile = File(...)):
    """ Recibe una imagen y la envía al servicio de preprocesamiento """
    image_data = BytesIO(await file.read())
    processed_image = await preprocessing_service.preprocess_image(image_data)
    return StreamingResponse(processed_image, media_type="image/jpeg")

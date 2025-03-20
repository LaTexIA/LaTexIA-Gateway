from fastapi import APIRouter, File, UploadFile, Depends
from app.adapters.latex_recognition_service import recognize_formula

router = APIRouter(prefix="/recognition", tags=["Recognition"])

@router.post("/latex")
async def latex_recognition(file: UploadFile = File(...)):
    result = await recognize_formula(await file.read())
    return {"latex_code": result["latex_code"]}

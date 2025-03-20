from fastapi import APIRouter

router = APIRouter(prefix="/frontend", tags=["Frontend"])

@router.get("/status")
async def status():
    return {"message": "Frontend conectado al API Gateway"}

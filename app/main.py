from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from app.routes.preprocessing_routes import router as preprocessing_router
from app.routes.prediction_routes import router as prediction_router

app = FastAPI()

# Configurar FastAPI para servir archivos estáticos desde la carpeta /static
app.mount("/static", StaticFiles(directory="app/static"), name="static")

#registrar rutas
app.include_router(preprocessing_router)
app.include_router(prediction_router)

# Ruta para la página de bienvenida
@app.get("/")
async def read_root():
    return FileResponse("app/static/index.html")

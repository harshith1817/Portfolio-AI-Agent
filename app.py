from fastapi import FastAPI

from api.schemas import ChatRequest
from api.routes import router
from core.config import APP_NAME, APP_VERSION

app = FastAPI(
    title=APP_NAME,
    version=APP_VERSION
)

app.include_router(router)
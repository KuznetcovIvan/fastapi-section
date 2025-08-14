from fastapi import FastAPI
from app.config import settings
from app.api import spimex_router
from app.db import prepare_models

app = FastAPI(title=settings.app_title, description=settings.description)
app.include_router(spimex_router)


@app.on_event('startup')
async def startup():
    await prepare_models()

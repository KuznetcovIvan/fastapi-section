from fastapi import FastAPI
from app.config import settings
from app.api import spimex_router
from app.db import engine, map_trading_results

app = FastAPI(title=settings.app_title, description=settings.description)
app.include_router(spimex_router)


@app.on_event('startup')
async def startup():
    async with engine.begin() as connection:
        await connection.run_sync(map_trading_results)

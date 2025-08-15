import redis.asyncio as redis
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from fastapi import FastAPI
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend

from app.api import spimex_router
from app.config import settings
from app.db import engine, map_trading_results
from app.tasks import clear_cache_task

app = FastAPI(title=settings.app_title, description=settings.description)
app.include_router(spimex_router)

redis_client = redis.from_url(settings.redis_cache_url)
scheduler = AsyncIOScheduler()

FastAPICache.init(
    RedisBackend(redis_client), prefix='spimex', expire=settings.expire_cache
)


@app.on_event('startup')
async def startup():
    async with engine.begin() as connection:
        await connection.run_sync(map_trading_results)

    scheduler.add_job(
        clear_cache_task, CronTrigger(hour=14, minute=11), id='clear_cache'
    )
    scheduler.start()

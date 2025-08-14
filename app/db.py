from sqlalchemy.ext.automap import automap_base
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from app.config import settings


engine = create_async_engine(settings.database_url)
AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession)

Base = automap_base()
TradingResults = None


async def prepare_models():
    global TradingResults
    async with engine.begin() as conn:
        def sync_prepare(sync_conn):
            Base.prepare(autoload_with=sync_conn)
        await conn.run_sync(sync_prepare)
    TradingResults = Base.classes.spimex_trading_results


async def get_async_session():
    async with AsyncSessionLocal() as session:
        yield session

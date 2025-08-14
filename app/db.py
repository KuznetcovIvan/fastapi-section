from sqlalchemy import Table
from sqlalchemy.orm import registry, sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from app.config import settings


engine = create_async_engine(settings.database_url)
AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession)


async def get_async_session():
    async with AsyncSessionLocal() as session:
        yield session


mapper_registry = registry()


class TradingResults:
    pass


def map_trading_results(connection):
    mapper_registry.map_imperatively(
        TradingResults, Table(settings.table_name,
                              mapper_registry.metadata,
                              autoload_with=connection)
    )

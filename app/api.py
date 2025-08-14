from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db import get_async_session, TradingResults
from app.schemas import TradingResultsDB

spimex_router = APIRouter()


@spimex_router.get('/', response_model=list[TradingResultsDB])
async def get_all(session: AsyncSession = Depends(get_async_session)):
    result = await session.execute(select(TradingResults).limit(20))
    return result.scalars().all()

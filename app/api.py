from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app import db
from app.db import get_async_session
from app.schemas import TradingResultsDB

spimex_router = APIRouter()


@spimex_router.get('/', response_model=list[TradingResultsDB])
async def get_all(session: AsyncSession = Depends(get_async_session)):
    model = db.TradingResults
    result = await session.execute(select(model).limit(20))
    return result.scalars().all()

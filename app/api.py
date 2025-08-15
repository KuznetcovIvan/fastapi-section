from datetime import date

from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession

from app.config import settings
from app.crud import get_trading_dates, read_trading_results_from_db
from app.db import get_async_session
from app.schemas import (
    DynamicTradingResultsQuery,
    TradingResultsDB,
    TradingResultsQuery,
)
from app.validators import query_filter_validators

spimex_router = APIRouter(prefix='/api')


@spimex_router.get(
    '/trading-dates',
    response_model=list[date],
    summary='Cписок дат последних торговых дней',
)
async def get_last_trading_dates(
    session: AsyncSession = Depends(get_async_session),
    days: int = Query(..., gt=0, le=settings.max_days_limit),
):
    return await get_trading_dates(session, days)


@spimex_router.get(
    '/results-by-date',
    response_model=list[TradingResultsDB],
    summary='Cписок торгов за заданный период',
)
async def get_dynamics(
    session: AsyncSession = Depends(get_async_session),
    filters: DynamicTradingResultsQuery = Depends(),
):
    return await read_trading_results_from_db(
        session, query_filter_validators(filters)
    )


@spimex_router.get(
    '/last-results',
    response_model=list[TradingResultsDB],
    summary='Cписок последних торгов',
)
async def get_trading_results(
    session: AsyncSession = Depends(get_async_session),
    filters: TradingResultsQuery = Depends(),
):
    return await read_trading_results_from_db(
        session, query_filter_validators(filters), last=True
    )

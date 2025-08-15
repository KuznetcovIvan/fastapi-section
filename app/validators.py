from datetime import timedelta
from fastapi import HTTPException
from app.config import settings
from app.schemas import TradingResultsQuery, DynamicTradingResultsQuery


def query_filter_validators(
    filters: TradingResultsQuery | DynamicTradingResultsQuery
):
    if isinstance(filters, DynamicTradingResultsQuery):
        if filters.start_date > filters.end_date:
            raise HTTPException(
                422,
                f'start_date={filters.start_date} '
                f'больше end_date={filters.end_date}'
            )
        if ((filters.end_date - filters.start_date)
                > timedelta(days=settings.max_days_range)):
            raise HTTPException(
                422,
                f'Выборка не может превышать {settings.max_days_range} дней'
            )
    return filters

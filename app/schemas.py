from pydantic import BaseModel, Field
from datetime import date


class TradingResultsDB(BaseModel):
    """Схема вывода результатов торгов."""
    exchange_product_id: str
    exchange_product_name: str
    oil_id: str
    delivery_basis_id: str
    delivery_basis_name: str
    delivery_type_id: str
    volume: int
    total: int
    count: int
    date: date

    class Config:
        orm_mode = True


class TradingResultsQuery(BaseModel):
    """Схема для фильтрации последних торгов."""
    oil_id: str | None = Field(None, min_length=4, max_length=4)
    delivery_type_id: str | None = Field(None, min_length=1, max_length=1)
    delivery_basis_id: str | None = Field(None, min_length=3, max_length=3)


class DynamicTradingResultsQuery(TradingResultsQuery):
    """Схема для фильтрации торгов за период."""
    start_date: date
    end_date: date

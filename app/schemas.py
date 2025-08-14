from pydantic import BaseModel, Extra, Field, root_validator
from datetime import date


class TradingResultsDB(BaseModel):
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
        title = 'Схема вывода результатов торгов'
        orm_mode = True


class TradingResultsQuery(BaseModel):
    oil_id: None | str = Field(None, min_length=4, max_length=4)
    delivery_type_id: None | str = Field(None, min_length=1, max_length=1)
    delivery_basis_id: None | str = Field(None, min_length=3, max_length=3)

    class Config:
        title = 'Схема для фильтрации последних торгов'
        extra = Extra.forbid


class DynamicTradingResultsQuery(TradingResultsQuery):
    start_date: date
    end_date: date

    class Config:
        title = 'Схема для фильтрации торгов за период'

    @root_validator
    def check_dates(cls, values):
        if values['start_date'] > values['end_date']:
            raise ValueError('start_date не может быть позже end_date')
        return values

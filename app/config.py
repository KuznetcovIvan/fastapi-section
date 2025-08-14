from pydantic import BaseSettings


class Settings(BaseSettings):
    app_title: str = 'SPIMEX API'
    description: str = 'Cервис для получения данных по итогам торгов'
    database_url: str
    table_name: str

    class Config:
        env_file = '.env'


settings = Settings()

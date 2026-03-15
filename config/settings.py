from pydantic import BaseModel

class Settings(BaseModel):
    data_start_date: str = '2025-06-01'
    date_end_date: str = '2026-06-02'
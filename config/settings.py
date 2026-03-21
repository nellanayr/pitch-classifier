from pydantic import BaseModel

class Settings(BaseModel):
    data_start_date: str = '2025-01-01'
    date_end_date: str = '2025-12-31'
    data_csv_path: str = 'data/pitches.csv'
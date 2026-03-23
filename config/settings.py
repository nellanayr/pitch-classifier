from pydantic import BaseModel

class Settings(BaseModel):
    # data
    data_start_date: str = '2025-01-01'
    date_end_date: str = '2025-12-31'
    data_csv_path: str = 'data/pitches.csv'

    # models
    random_seed: int = 19

    # multinomial linear regression
    mlr_test_prop: float = .25

from config import settings
import duckdb
import pandas as pd

SETTINGS = settings.Settings()
DATA_PATH = SETTINGS.data_csv_path

def get_data() -> pd.DataFrame:
    return duckdb.query(f"select * from '{DATA_PATH}'").to_df()
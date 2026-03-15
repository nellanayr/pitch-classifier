from config import settings
import pandas as pd
import pybaseball

pybaseball.cache.enable()
SETTINGS = settings.Settings()

def _get_statcast_data(
    start_date: str = SETTINGS.data_start_date, 
    end_date: str = SETTINGS.date_end_date
) -> pd.DataFrame:
    return pybaseball.statcast(start_dt = start_date, end_dt = end_date, verbose = False)

def _get_features(df: pd.DataFrame) -> pd.DataFrame:
    return df[[
        'pitch_type',
        'pitch_name',
        'p_throws',
        'release_speed',
        # 'release_spin',
        'pfx_x',
        'pfx_z',
        'spin_axis'
    ]]

def main():
    sc_df = _get_statcast_data()
    df = _get_features(df = sc_df)
    df.to_csv('data/pitches.csv', index = False)

if __name__ == '__main__':
    main()
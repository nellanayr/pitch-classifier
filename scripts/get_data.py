from config import settings
import duckdb
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
    df = df
    return duckdb.query(
        """
        select
            pitch_type,
            pitch_name,
            release_speed,
            case
                when p_throws = 'L' then pfx_x * -1
                else pfx_x
            end as pfx_x,                   -- standardize lefties and righties
            pfx_z,
            spin_axis 
        from df
        where 1=1
            and pitch_type != 'PO'          -- no pitchouts 
            and pitch_type is not null      -- remove missing data rows
        """
    ).to_df()

def main():
    sc_df = _get_statcast_data()
    df = _get_features(df = sc_df)
    df.to_csv(SETTINGS.data_csv_path, index = False)

if __name__ == '__main__':
    main()
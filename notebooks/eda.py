# yeah its not a notebook, sue me

from config import settings
import duckdb

SETTINGS = settings.Settings()
DATA_PATH = SETTINGS.data_csv_path

def _preview_data() -> None:
    print(
        duckdb.query(f"select * from '{DATA_PATH}' limit 10")
    )

def _overall_n() -> None:
    print(
        duckdb.query(f"select count(*) as n_rows from '{DATA_PATH}'")
    ) 

def _pitch_type_n() -> None:
    print(
        duckdb.query(
            f"""
            select 
                pitch_type, 
                count(*) as n_rows 
            from '{DATA_PATH}' 
            group by 1
            order by 2 desc
            """
        )
    )

def _pitch_type_vs_name() -> None:
    print(
        duckdb.query(
            f"""
            select distinct
                pitch_type,
                pitch_name
            from '{DATA_PATH}'
            order by 1
            """
        )
    )

def _check_null_data() -> None:
    print(
        duckdb.query(
            f"""
            select *
            from '{DATA_PATH}'
            where pitch_type is null
            """
        )
    )

def _velocity_by_pitch_type() -> None:
    print(
        duckdb.query(
            f"""
            select
                pitch_name,
                count(*) as n,
                min(release_speed) as min,
                quantile(release_speed, 0.25) as p25,
                quantile(release_speed, 0.50) as med,
                quantile(release_speed, 0.75) as p75,
                max(release_speed) as max
            from '{DATA_PATH}'
            group by 1
            order by 2 desc
            """
        )
    )

def main():
    # data preview
    print('Preview Data')
    _preview_data()
    print()

    # counts
    print(f'# of Pitches')
    _overall_n()
    print()

    print(f'# of Pitches by Pitch Type')
    _pitch_type_n()
    print()

    # checks
    print('Checking relationship between pitch_type and pitch_name')
    _pitch_type_vs_name()
    print()
    # 1 to 1; no need to bring analyze separately

    print('Checking NULL rows')
    _check_null_data()
    print()
    # missing data; i.e., not "unclassified"

    # distributions
    print('Velocity by Pitch Type')
    _velocity_by_pitch_type()
    print()
    

if __name__ == '__main__':
    main()
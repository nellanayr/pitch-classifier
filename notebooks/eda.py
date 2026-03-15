# yeah its not a notebook, sue me

import duckdb
import pandas as pd

def _import_data() -> pd.DataFrame():
    return duckdb.query("select * from 'data/pitches.csv'").to_df()

def _overall_n(df: pd.DataFrame) -> int:
    return len(df)

def main():
    # data preview
    print('Preview Data')
    df = _import_data()
    print(df.head(10))
    print()

    # counts
    print(f'# of Pitches: {_overall_n(df = df)}')

if __name__ == '__main__':
    main()
import pybaseball

START_DATE = '2025-06-01'
END_DATE = '2026-06-30'

df = pybaseball.statcast_pitcher(start_dt = START_DATE, end_dt = END_DATE)
print(df.head(10))
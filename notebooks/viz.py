from config import settings
import duckdb
import matplotlib.pyplot as plt
import pandas as pd

SETTINGS = settings.Settings()
DATA_PATH = SETTINGS.data_csv_path

def _get_data() -> pd.DataFrame:
    return duckdb.query(f"select * from '{DATA_PATH}'").to_df()

def velo_dist_bw(df: pd.DataFrame) -> None:
    df = df.copy()
    output_path = 'visualizations/velo_dist_bw.png'
    # Clean types for plotting
    df["release_speed"] = pd.to_numeric(df["release_speed"], errors="coerce")
    df = df[df["pitch_name"].notna() & df["release_speed"].notna()]
    # Order pitches by median release_speed
    med = (
        df.groupby("pitch_name")["release_speed"]
          .median()
          .sort_values(ascending=False)  # change to False for descending
    )
    pitch_names = med.index.tolist()
    data_by_pitch = [
        df.loc[df["pitch_name"] == pitch, "release_speed"].to_numpy()
        for pitch in pitch_names
    ]
    fig_w = max(10, 0.6 * len(pitch_names))
    fig, ax = plt.subplots(figsize=(fig_w, 6))
    ax.boxplot(
        data_by_pitch,
        tick_labels=pitch_names,
        showfliers=True,
        flierprops={
            "marker": "o",
            "markersize": 3,
            "alpha": 0.25,            
            "markerfacecolor": "gray",
            "markeredgecolor": "gray",
        },
    )
    ax.set_ylabel("Release Speed")
    ax.set_title("Velocity Distribution by Pitch (ordered by median)")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    fig.savefig(output_path, dpi=200)
    plt.close(fig)

def main():
    # import df
    df = _get_data()

    # box and whisker of velo distributions
    velo_dist_bw(df = df)

if __name__ == '__main__':
    main()
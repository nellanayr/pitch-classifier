from utils import common
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

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

def break_scatter(df: pd.DataFrame) -> None:
    df = df.copy()
    output_path = "visualizations/break_scatter.png"
    df["pfx_x"] = pd.to_numeric(df["pfx_x"], errors="coerce")
    df["pfx_z"] = pd.to_numeric(df["pfx_z"], errors="coerce")
    df = df[
        df["pitch_name"].notna()
        & df["pfx_x"].notna()
        & df["pfx_z"].notna()
    ]
    pitches = sorted(df["pitch_name"].unique())

    # One color per pitch (cycles tab10 if >10 types)
    base_colors = plt.cm.tab10(np.linspace(0, 1, 10))
    color_map = {p: base_colors[i % 10] for i, p in enumerate(pitches)}
    fig, ax = plt.subplots(figsize=(10, 8))
    # Raw points: light / dense
    for pitch in pitches:
        sub = df.loc[df["pitch_name"] == pitch]
        ax.scatter(
            sub["pfx_x"],
            sub["pfx_z"],
            c=[color_map[pitch]],
            s=15,
            alpha=0.25,
            edgecolors="none",
            label=pitch,
        )
    # Mean per pitch: bolder overlay
    means = df.groupby("pitch_name", observed=True)[["pfx_x", "pfx_z"]].mean()
    for pitch in pitches:
        if pitch not in means.index:
            continue
        row = means.loc[pitch]
        ax.scatter(
            row["pfx_x"],
            row["pfx_z"],
            c=[color_map[pitch]],
            s=120,
            alpha=1.0,
            edgecolors="black",
            linewidths=1.5,
            zorder=5,
        )
    ax.set_xlabel("pfx_x")
    ax.set_ylabel("pfx_z")
    ax.set_title("Pitch movement: pfx_x vs pfx_z")
    ax.axhline(0, color="black", linewidth=2, zorder=100)
    ax.axvline(0, color="black", linewidth=2, zorder=100)
    ax.legend(bbox_to_anchor=(1.02, 1), loc="upper left", fontsize=8)
    plt.tight_layout()
    fig.savefig(output_path, dpi=200, bbox_inches="tight")
    plt.close(fig)

def main():
    # import df
    df = common.get_data()

    # box and whisker of velo distributions
    velo_dist_bw(df = df)

    # scatter plot of pitch breaks
    break_scatter(df = df)

if __name__ == '__main__':
    main()
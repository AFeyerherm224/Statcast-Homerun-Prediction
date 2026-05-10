import pandas as pd

def load_data(filepath):
    """
    Load raw Statcast data from CSV.
    """
    return pd.read_csv(filepath)


def clean_data(df):
    """
    Drop missing or invalid rows
    Standardize column names
    """
    df = df.dropna()

    df.columns = [col.lower().replace(" ", "_") for col in df.columns]

    return df


def merge_datasets(hitters_df, pitchers_df, games_df):
    """
    Merge hitter, pitcher, and game-level datasets
    into a single modeling table.
    """
    df = hitters_df.merge(games_df, on="game_id", how="left")
    df = df.merge(pitchers_df, on=["game_id", "pitcher_id"], how="left")

    return df


def run_pipeline(hitter_path, pitcher_path, game_path):
    hitters = load_data(hitter_path)
    pitchers = load_data(pitcher_path)
    games = load_data(game_path)

    hitters = clean_data(hitters)
    pitchers = clean_data(pitchers)
    games = clean_data(games)

    return merge_datasets(hitters, pitchers, games)
import pandas as pd

def add_hitter_features(df):
    """
    Create hitter-based features.
    """
    df["exit_velocity_avg"] = df.groupby("batter_id")["exit_velocity"].transform("mean")
    df["launch_angle_avg"] = df.groupby("batter_id")["launch_angle"].transform("mean")

    return df


def add_pitcher_features(df):
    """
    Create pitcher-based features.
    """
    df["pitcher_hr_rate"] = df.groupby("pitcher_id")["home_run_allowed"].transform("mean")

    return df


def add_context_features(df):
    """
    Add contextual features like ballpark effects.
    """
    df["is_favorable_park"] = df["stadium_factor"] > df["stadium_factor"].median()

    return df


def build_features(df):
    df = add_hitter_features(df)
    df = add_pitcher_features(df)
    df = add_context_features(df)

    return df
import pandas as pd


def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    """Drop rows missing any feature/label value (keeps 'id' optional)."""
    df = df.copy()
    key_columns = [col for col in df.columns if col.lower() != "id"]
    return df.dropna(subset=key_columns).reset_index(drop=True)

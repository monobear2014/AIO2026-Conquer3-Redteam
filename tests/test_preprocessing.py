import pandas as pd

from src.preprocessing import preprocess_data


def test_preprocess_data_runs_and_returns_non_empty():
    df = pd.DataFrame(
        {
            "age": [25, 30, 40],
            "flight_distance": [100, 200, 300],
            "satisfaction": ["satisfied", "neutral", "dissatisfied"],
        }
    )

    result = preprocess_data(df)

    assert not result.empty


def test_preprocess_data_drops_missing_values():
    df = pd.DataFrame(
        {
            "age": [25, 30, None, 40],
            "flight_distance": [100, 200, 300, None],
            "satisfaction": ["satisfied", "neutral", "satisfied", "dissatisfied"],
        }
    )

    result = preprocess_data(df)

    assert result.isnull().sum().sum() == 0
    assert len(result) == 2

import pandas as pd
from pathlib import Path


def preprocess_data(dataset_file: Path):
    data = pd.read_csv(dataset_file)

    # Define features and target
    X = data.drop(columns=["rental_price_per_day", "Unnamed: 0"])
    y = data["rental_price_per_day"]

    # save to files as backup
    X.to_csv("data/X.csv", index=False)
    y.to_csv("data/y.csv", index=False)

    return X, y

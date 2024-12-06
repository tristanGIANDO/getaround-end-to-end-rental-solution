from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.compose import ColumnTransformer
import pickle
import pandas as pd
from pathlib import Path


def create_model(preprocessor: ColumnTransformer) -> Pipeline:
    # Create a pipeline with a RandomForestRegressor
    model = Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            ("regressor", RandomForestRegressor(random_state=42)),
        ]
    )
    return model


def evaluate_model(model: Pipeline, X: pd.DataFrame, y: pd.Series) -> float:
    # Split the data into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    print(y_test)

    # Train the model
    model.fit(X_train, y_train)

    # Evaluate the model
    y_pred = model.predict(X_test)

    # Save the trained model
    model_path = Path("data/model.pkl")
    with open(model_path, "wb") as file:
        pickle.dump(model, file)

    return mean_squared_error(y_test, y_pred)

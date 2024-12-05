from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
import pandas as pd


def create_pipeline(X: pd.DataFrame) -> ColumnTransformer:
    # Identify categorical and numerical columns
    categorical_columns = X.select_dtypes(include=["object", "bool"]).columns
    numerical_columns = X.select_dtypes(include=["int64", "float64"]).columns

    # Preprocessing for numerical data
    numerical_transformer = SimpleImputer(strategy="mean")

    # Preprocessing for categorical data
    categorical_transformer = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("onehot", OneHotEncoder(handle_unknown="ignore")),
        ]
    )

    # Combine preprocessors in a column transformer
    return ColumnTransformer(
        transformers=[
            ("num", numerical_transformer, numerical_columns),
            ("cat", categorical_transformer, categorical_columns),
        ]
    )

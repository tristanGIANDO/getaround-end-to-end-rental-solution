from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

# Load the CSV data
data_path = "resources/get_around_pricing_project.csv"
data = pd.read_csv(data_path)

# Define features and target
X = data.drop(columns=["rental_price_per_day", "Unnamed: 0"])
y = data["rental_price_per_day"]

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
preprocessor = ColumnTransformer(
    transformers=[
        ("num", numerical_transformer, numerical_columns),
        ("cat", categorical_transformer, categorical_columns),
    ]
)

# Create a pipeline with a RandomForestRegressor
model = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        ("regressor", RandomForestRegressor(random_state=42)),
    ]
)

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# save x_train to file
X_train.to_csv("data/X_train.csv", index=False)
X_test.to_csv("data/X_test.csv", index=False)
y_train.to_csv("data/y_train.csv", index=False)
y_test.to_csv("data/y_test.csv", index=False)

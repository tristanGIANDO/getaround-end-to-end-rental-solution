from pathlib import Path
from models.preprocessing import preprocess_data
from models.pipeline import create_pipeline
from models.model_training_evaluation import create_model, evaluate_model

X, y = preprocess_data(Path("resources/get_around_pricing_project.csv"))
preprocessor = create_pipeline(X)
model = create_model(preprocessor)
mse = evaluate_model(model, X, y)
print(f"Mean Squared Error: {mse}")

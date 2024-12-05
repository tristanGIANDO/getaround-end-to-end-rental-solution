from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pickle
import numpy as np
from typing import List
from pathlib import Path

# Load the pre-trained machine learning model
MODEL_PATH = Path("data/model.pkl")
with open(MODEL_PATH, "rb") as model_file:
    model = pickle.load(model_file)

app = FastAPI()


class PredictionRequest(BaseModel):
    input: List[List[float]]


class PredictionResponse(BaseModel):
    prediction: List[float]


@app.post("/predict", response_model=PredictionResponse)
def predict(request: PredictionRequest):
    """
    Endpoint to make predictions.
    Expects a JSON payload with key 'input' containing a 2D list of features.
    """
    try:
        inputs = np.array(request.input)
        predictions = model.predict(inputs).tolist()
        return PredictionResponse(prediction=predictions)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# Dockerfile configuration and deployment for Heroku
# Dockerfile
# FROM python:3.9-slim
# WORKDIR /app
# COPY requirements.txt requirements.txt
# RUN pip install -r requirements.txt
# COPY . .
# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

# Deployment to Heroku Steps
# 1. Create a `requirements.txt` file with all dependencies.
# 2. Build and push the Docker image to Heroku:
#    heroku container:push web --app <your-app-name>
# 3. Release the Docker image:
#    heroku container:release web --app <your-app-name>
# 4. Access the app at: https://<your-app-name>.herokuapp.com

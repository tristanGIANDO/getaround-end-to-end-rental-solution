import os
from typing import Union

import pandas as pd
import uvicorn
from fastapi import FastAPI, Request
from joblib import load
from pydantic import BaseModel

app = FastAPI()


class PredictionFeatures(BaseModel):
    model_key: str
    mileage: Union[int, float]
    engine_power: Union[int, float]
    fuel: str
    paint_color: str
    car_type: str
    private_parking_available: bool
    has_gps: bool
    has_air_conditioning: bool
    automatic_car: bool
    has_getaround_connect: bool
    has_speed_regulator: bool
    winter_tires: bool


@app.post("/predict", tags=["Predictions"], summary="Predict rental price")
async def predict(
    input_data: PredictionFeatures, request: Request
) -> set[str] | dict[str, str]:
    await request.json()

    try:
        model = load("model.pkl")

        # Préparer les données d'entrée sous forme de DataFrame
        features = {
            "model_key": [input_data.model_key],
            "mileage": [input_data.mileage],
            "engine_power": [input_data.engine_power],
            "fuel": [input_data.fuel],
            "paint_color": [input_data.paint_color],
            "car_type": [input_data.car_type],
            "private_parking_available": [input_data.private_parking_available],
            "has_gps": [input_data.has_gps],
            "has_air_conditioning": [input_data.has_air_conditioning],
            "automatic_car": [input_data.automatic_car],
            "has_getaround_connect": [input_data.has_getaround_connect],
            "has_speed_regulator": [input_data.has_speed_regulator],
            "winter_tires": [input_data.winter_tires],
        }
        input_df = pd.DataFrame(features)  # Convertir en DataFrame

        # Effectuer la prédiction
        prediction_result = model.predict(input_df)

        # Retourner le résultat de la prédiction
        return {"prediction": f"{prediction_result[0]:.2f}$"}

    except Exception as e:
        print(f"Error during processing: {e}")
        return {"error": str(e)}


if __name__ == "__main__":
    import uvicorn

    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)

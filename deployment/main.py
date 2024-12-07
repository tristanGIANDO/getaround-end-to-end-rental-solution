import os
from typing import Union

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
        prediction_result = model.predict(input_data)

        return {f"{prediction_result[0]:.2f}$"}

    except Exception as e:
        print(f"Error during processing: {e}")
        return {"error": str(e)}


if __name__ == "__main__":
    import uvicorn

    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)

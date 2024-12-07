import json
import subprocess

url = "https://gtgetaroundapi-2a820dfe259d.herokuapp.com/predict"
headers = {"Content-Type": "application/json"}
payload = {
    "model_key": "Renault",
    "mileage": 77334,
    "engine_power": 256,
    "fuel": "diesel",
    "paint_color": "black",
    "car_type": "coupe",
    "private_parking_available": True,
    "has_gps": False,
    "has_air_conditioning": True,
    "automatic_car": False,
    "has_getaround_connect": False,
    "has_speed_regulator": True,
    "winter_tires": False,
}

command = [
    "curl",
    "-X",
    "POST",
    url,
    "-H",
    "Content-Type: application/json",
    "-d",
    json.dumps(payload),
]

# Exécuter la commande et capturer la sortie
result = subprocess.run(command, capture_output=True, text=True)

# Afficher la réponse
print("Response:", result.stdout)
print("Error:", result.stderr)

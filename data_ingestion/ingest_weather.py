import requests
import pandas as pd
from pathlib import Path

LAT, LON = 31.04, 31.38  # الدقهلية - الدلتا
START, END = "2024-01-01", "2025-12-31"

URL = "https://archive-api.open-meteo.com/v1/archive"
params = {
    "latitude": LAT,
    "longitude": LON,
    "start_date": START,
    "end_date": END,
    "hourly": ",".join([
        "temperature_2m",
        "relative_humidity_2m",
        "precipitation",
        "et0_fao_evapotranspiration",
        "soil_moisture_0_to_7cm",
        "soil_temperature_0_to_7cm",
    ]),
    "timezone": "Africa/Cairo",
}

r = requests.get(URL, params=params, timeout=60)
r.raise_for_status()

df = pd.DataFrame(r.json()["hourly"])
Path("data/raw").mkdir(parents=True, exist_ok=True)
df.to_csv("data/raw/weather_soil_delta.csv", index=False)

print(df.shape)
print(df.head())
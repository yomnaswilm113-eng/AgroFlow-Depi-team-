import time
import requests
import pandas as pd
from pathlib import Path

LOCATIONS = {
    "Dakahlia":    (31.04, 31.38),
    "Gharbia":     (30.79, 31.00),
    "KafrElSheikh": (31.11, 30.94),
}
START, END = "2021-01-01", "2025-12-31"

URL = "https://archive-api.open-meteo.com/v1/archive"
HOURLY = [
    "temperature_2m",
    "relative_humidity_2m",
    "precipitation",
    "et0_fao_evapotranspiration",
    "shortwave_radiation",
    "wind_speed_10m",
    "soil_moisture_0_to_7cm",
    "soil_moisture_7_to_28cm",
    "soil_temperature_0_to_7cm",
    "soil_temperature_7_to_28cm",
]

frames = []
for name, (lat, lon) in LOCATIONS.items():
    params = {
        "latitude": lat,
        "longitude": lon,
        "start_date": START,
        "end_date": END,
        "hourly": ",".join(HOURLY),
        "timezone": "Africa/Cairo",
    }
    for attempt in range(3):
        r = requests.get(URL, params=params, timeout=120)
        if r.status_code == 200:
            break
        print(f"{name}: status {r.status_code}, retrying in 60s...")
        time.sleep(60)
    r.raise_for_status()

    df = pd.DataFrame(r.json()["hourly"])
    df.insert(0, "location", name)
    df.insert(1, "latitude", lat)
    df.insert(2, "longitude", lon)
    frames.append(df)
    print(name, df.shape)
    time.sleep(5)

out = pd.concat(frames, ignore_index=True)
Path("data/raw").mkdir(parents=True, exist_ok=True)
out.to_csv("data/raw/weather_soil_delta_multi.csv", index=False)
print("Total:", out.shape)
# Data Sources

## 1. Open-Meteo Historical Weather API
- Link: https://open-meteo.com (archive-api.open-meteo.com/v1/archive)
- Location: Dakahlia, Nile Delta (lat 31.04, lon 31.38)
- Period: 2024-01-01 to 2025-12-31, hourly (17,544 rows)
- Collection method: Python script `ingest_weather.py`
- File: data/raw/weather_soil_delta.csv

| Column | Description | Unit |
|---|---|---|
| time | Timestamp (Africa/Cairo) | datetime |
| temperature_2m | Air temperature at 2m | °C |
| relative_humidity_2m | Relative humidity | % |
| precipitation | Rainfall | mm |
| et0_fao_evapotranspiration | Reference evapotranspiration | mm |
| soil_moisture_0_to_7cm | Soil moisture (0-7cm) | m³/m³ |
| soil_temperature_0_to_7cm | Soil temperature (0-7cm) | °C |

## 2. Smart Irrigation - S14 IoT Dataset (Kaggle)
- Link: https://www.kaggle.com/datasets/srishtiprogrammer/smart-irrigation-s14-iot-dataset
- Author: Srishti Programmer
- Period: 2023-2024, hourly (16,128 rows, 8 columns)
- Collection method: manual download, converted by `ingest_irrigation.py`
- File: data/raw/irrigation_labels.csv
- Note: no description on Kaggle; data appears synthetic/simulated.

| Column | Description | Unit |
|---|---|---|
| timestamp | Timestamp | datetime |
| soil_resistance | Soil resistance reading | raw sensor value |
| temperature_C | Air temperature | °C |
| humidity_pct | Air humidity | % |
| rain_flag | Rain detected | 0/1 |
| pump_actual | Pump on (target label) | 0/1 |
| pump_predicted | Prediction from another model (excluded from training) | 0/1 |
| predicted_confidence | Confidence of that prediction (excluded) | 0-1 |

## Known issues (for Cleaning Engineer)
- Timestamp range/row count suggests possible day/month parsing mix-up.
- Dataset 2 locations/units are unknown; the two datasets do not share a time period or location.

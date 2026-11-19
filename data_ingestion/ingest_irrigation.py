import pandas as pd
from pathlib import Path

SRC = "data/raw/smart irrigation dataset.xlsx"
OUT = "data/raw/irrigation_labels.csv"

df = pd.read_excel(SRC)
Path("data/raw").mkdir(parents=True, exist_ok=True)
df.to_csv(OUT, index=False)

print("Shape:", df.shape)
print("Columns:", list(df.columns))
print("Date range:", df["timestamp"].min(), "->", df["timestamp"].max())
print("Missing values:", int(df.isna().sum().sum()))
print("Label balance:")
print(df["pump_actual"].value_counts())
import json
import joblib
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

model = joblib.load(BASE_DIR / "models" / "security_model.pkl")

dataset = pd.read_csv(BASE_DIR / "data" / "training_dataset.csv")

prediction = model.predict(dataset[["records"]])

dataset["prediction"] = prediction

output = BASE_DIR / "output" / "prediction.json"

dataset.to_json(output, orient="records", indent=4)

print("=" * 50)
print("Prediction Completed")
print(output)
print("=" * 50)

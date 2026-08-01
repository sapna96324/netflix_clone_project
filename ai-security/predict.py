import joblib
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

MODEL_FILE = BASE_DIR / "models" / "security_model.pkl"

OUTPUT_DIR = BASE_DIR / "output"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

OUTPUT_FILE = OUTPUT_DIR / "prediction.csv"

DATASET = BASE_DIR / "data" / "training_dataset.csv"

model = joblib.load(MODEL_FILE)

df = pd.read_csv(DATASET)

prediction = model.predict(df[["records"]])

df["prediction"] = prediction

df.to_csv(OUTPUT_FILE, index=False)

print("=" * 50)
print("Prediction Completed")
print(f"Prediction saved at: {OUTPUT_FILE}")
print("=" * 50)

import pandas as pd
import joblib
from pathlib import Path
from sklearn.tree import DecisionTreeClassifier

BASE_DIR = Path(__file__).resolve().parent

DATASET = BASE_DIR / "data" / "training_dataset.csv"

MODELS_DIR = BASE_DIR / "models"
MODELS_DIR.mkdir(parents=True, exist_ok=True)

MODEL_FILE = MODELS_DIR / "security_model.pkl"

df = pd.read_csv(DATASET)

# Features
X = df[["records"]]

# Labels
y = df["risk"]

model = DecisionTreeClassifier(random_state=42)

model.fit(X, y)

joblib.dump(model, MODEL_FILE)

print("=" * 50)
print("AI Model Trained Successfully")
print(f"Model saved at: {MODEL_FILE}")
print("=" * 50)

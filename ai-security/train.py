import pandas as pd
import joblib
from pathlib import Path
from sklearn.tree import DecisionTreeClassifier

BASE_DIR = Path(__file__).resolve().parent

dataset = BASE_DIR / "data" / "training_dataset.csv"
model_file = BASE_DIR / "models" / "security_model.pkl"

df = pd.read_csv(dataset)

# Features
X = df[["records"]]

# Labels
y = df["risk"]

model = DecisionTreeClassifier(random_state=42)

model.fit(X, y)

joblib.dump(model, model_file)

print("=" * 50)
print("Model trained successfully")
print(model_file)
print("=" * 50)

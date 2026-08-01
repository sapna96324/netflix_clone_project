import json
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

merged_file = BASE_DIR / "data" / "merged_reports.json"
dataset_file = BASE_DIR / "data" / "training_dataset.csv"

with open(merged_file, "r") as f:
    reports = json.load(f)

rows = []

for tool, report in reports.items():

    rows.append({
        "tool": tool,
        "records": len(str(report)),
        "risk": 0
    })

df = pd.DataFrame(rows)

df.to_csv(dataset_file, index=False)

print(df)

print("\nDataset Created")

print(dataset_file)

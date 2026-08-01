import json
import os

BASE_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..")
)

REPORTS = {
    "sonarqube": os.path.join(
        BASE_DIR,
        "security",
        "sonarqube",
        "sonar-report.json"
    ),

    "trivy": os.path.join(
        BASE_DIR,
        "security",
        "trivy",
        "trivy-report.json"
    ),

    "dependency_check": os.path.join(
        BASE_DIR,
        "security",
        "dependency-check",
        "dependency-check-report.json"
    ),

    "zap": os.path.join(
        BASE_DIR,
        "security",
        "zap",
        "zap-report.json"
    )
}

merged = {}

for name, path in REPORTS.items():

    print(f"Reading {name}...")

    if os.path.exists(path):

        try:

            with open(path, "r", encoding="utf-8") as f:
                merged[name] = json.load(f)

            print(f"✓ {name} loaded")

        except Exception as e:

            print(f"Error reading {name}: {e}")

            merged[name] = {}

    else:

        print(f"Missing: {path}")

        merged[name] = {}

OUTPUT = os.path.join(
    BASE_DIR,
    "ai-security",
    "data",
    "merged_reports.json"
)

with open(OUTPUT, "w", encoding="utf-8") as f:
    json.dump(merged, f, indent=4)

print("\nMerged report created successfully")
print(OUTPUT)

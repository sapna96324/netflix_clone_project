import json
import os

ARTIFACT_DIR = "/var/jenkins_home/devsecops-artifacts"

REPORTS = {
    "sonarqube": os.path.join(
        ARTIFACT_DIR,
        "sonarqube",
        "sonar-report.json"
    ),

    "trivy": os.path.join(
        ARTIFACT_DIR,
        "trivy",
        "trivy-report.json"
    ),

    "dependency_check": os.path.join(
        ARTIFACT_DIR,
        "dependency-check",
        "dependency-check-report.json"
    ),

    "zap": os.path.join(
        ARTIFACT_DIR,
        "zap",
        "zap-report.json"
    )
}

merged = {}

for tool, path in REPORTS.items():

    print(f"Reading {tool}...")

    if os.path.exists(path):

        try:

            with open(path, "r", encoding="utf-8") as f:
                merged[tool] = json.load(f)

            print(f"✓ Loaded {tool}")

        except Exception as e:

            print(f"Error reading {tool}: {e}")

            merged[tool] = {}

    else:

        print(f"Missing: {path}")

        merged[tool] = {}

BASE = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

OUTPUT = os.path.join(
    BASE,
    "data",
    "merged_reports.json"
)

os.makedirs(
    os.path.dirname(OUTPUT),
    exist_ok=True
)

with open(
    OUTPUT,
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        merged,
        f,
        indent=4
    )

print("")
print("======================================")
print("Merged report created successfully")
print(OUTPUT)
print("======================================")

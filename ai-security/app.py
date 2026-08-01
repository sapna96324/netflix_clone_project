from flask import Flask, render_template, send_from_directory
import json
import pandas as pd
import os

app = Flask(__name__)

BASE = os.path.dirname(os.path.abspath(__file__))

MERGED = os.path.join(BASE, "data", "merged_reports.json")
PREDICT = os.path.join(BASE, "output", "prediction.csv")


@app.route("/")
def dashboard():

    reports = {}
    prediction = {}

    if os.path.exists(MERGED):
        with open(MERGED, "r", encoding="utf-8") as f:
            reports = json.load(f)

    if os.path.exists(PREDICT):
        df = pd.read_csv(PREDICT)
        if not df.empty:
            prediction = df.iloc[0].to_dict()

    # ----------------------------
    # SonarQube
    # ----------------------------

    sonar_total = len(
        reports.get("sonarqube", {}).get("issues", [])
    )

    # ----------------------------
    # Trivy
    # ----------------------------

    trivy_total = 0

    trivy = reports.get("trivy", {})

    if isinstance(trivy, list):
        for image in trivy:
            for result in image.get("Results", []):
                trivy_total += len(
                    result.get("Vulnerabilities", [])
                )

    # ----------------------------
    # Dependency Check
    # ----------------------------

    dependency_total = len(
        reports.get("dependency_check", {}).get("dependencies", [])
    )

    # ----------------------------
    # ZAP
    # ----------------------------

    zap_total = len(
        reports.get("zap", {}).get("site", [])
    )

    # ----------------------------
    # Overall Total
    # ----------------------------

    total_findings = (
        sonar_total +
        trivy_total +
        dependency_total +
        zap_total
    )

    # ----------------------------
    # Risk Score
    # ----------------------------

    risk_score = min(total_findings, 100)

    if risk_score >= 80:
        risk_level = "HIGH"

    elif risk_score >= 40:
        risk_level = "MEDIUM"

    else:
        risk_level = "LOW"

    return render_template(

        "dashboard.html",

        reports=reports,

        prediction=prediction,

        sonar_total=sonar_total,

        trivy_total=trivy_total,

        dependency_total=dependency_total,

        zap_total=zap_total,

        total_findings=total_findings,

        risk_score=risk_score,

        risk_level=risk_level
    )

@app.route("/download/<report>")
def download_report(report):

    REPORTS = {
    "sonar": (
        os.path.join(BASE, "data", "reports", "sonarqube"),
        "sonar-report.json"
    ),

    "trivy": (
        os.path.join(BASE, "data", "reports", "trivy"),
        "trivy-report.json"
    ),

    "dependency": (
        os.path.join(BASE, "data", "reports", "dependency-check"),
        "dependency-check-report.json"
    ),

    "zap": (
        os.path.join(BASE, "data", "reports", "zap"),
        "zap-report.json"
    ),

    "ai": (
        os.path.join(BASE, "output"),
        "security_report.html"
    )
}

  

    if report not in REPORTS:
        return "Report not found", 404

    folder, filename = REPORTS[report]

    return send_from_directory(
        folder,
        filename,
        as_attachment=True
    )



if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )

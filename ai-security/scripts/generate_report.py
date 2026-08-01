import pandas as pd
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent

prediction = pd.read_csv(BASE / "output" / "prediction.csv")

html = f"""
<html>
<head>
<title>Netflix AI Security Report</title>
<style>
body {{
font-family: Arial;
margin:40px;
}}

table {{
border-collapse: collapse;
width:100%;
}}

th,td {{
border:1px solid black;
padding:10px;
text-align:center;
}}

th {{
background:#222;
color:white;
}}

h1 {{
color:#d62828;
}}

</style>
</head>

<body>

<h1>Netflix AI Security Report</h1>

<h2>Prediction Results</h2>

{prediction.to_html(index=False)}

</body>

</html>
"""

report = BASE / "output" / "security_report.html"

report.write_text(html)

print(report)

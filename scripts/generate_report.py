import pandas as pd
from src.report_generator import generate_report

telemetry_data = pd.read_csv('data/telemetry_data.csv')
power_data = pd.read_csv('data/power_data.csv')

report = generate_report(telemetry_data, power_data)
with open('report.txt', 'w') as f:
    f.write(report)

print("Report generated.")

def generate_report(telemetry_data, power_data):
    report = "Power Measurement Report\n"
    report += "========================\n\n"
    report += "Telemetry Data:\n"
    report += telemetry_data.to_string()
    report += "\n\nPower Data:\n"
    report += power_data.to_string()
    return report

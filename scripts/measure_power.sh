#!/bin/bash
echo "Measuring power utilization..."
python3 src/system_utilization.py --utilization 100
python3 src/power_telemetry.py --output data/power_data.csv
echo "Power utilization measured."

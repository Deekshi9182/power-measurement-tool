#!/bin/bash
echo "Collecting initial telemetry data..."
python3 src/power_telemetry.py --output data/telemetry_data.csv
echo "Telemetry data collected."

"""
Detect valid, invalid, or suspicious readings, and clean them.

Input: Individual sensor .txt files
Output: Validated and cleaned data, and an invalid readings file
"""

from pathlib import Path
import datetime as dt
import json

required_fields = ["sensor_id", "timestamp", "temperature", "pressure", "windspeed"]
readings_data = Path("data\\output\\")

# Maximum allowed values
max_tempC = 40
max_pressure = 1100
max_windspeed = 40

# Minimum allowed values
min_tempC = -60
min_pressure = 100
min_windspeed = 0

# def validate(readings_data):
    
# This method should check if any fields are missing
# Check and ensure that a given jsonl reading has valid data types and are within standard acceptable ranges (stores in variables above)
def validate_readings_jsonl(sensor_file):
    sensor_file = Path(sensor_file)

    if sensor_file.suffix.lower() != ".jsonl":
        raise ValueError("Unsupported file type, please use JSONL.")

    valid_readings = []
    invalid_readings = []

    with open(sensor_file, mode="r", encoding="utf-8") as reading:
        for line_n, line in enumerate(reading, start=1):
            record = json.loads(line)

            # Find any missing fields
            missing_fields = [
                field for field in required_fields
               if field not in record or record[field] in (None, "")
            ]

            # If there's missing fields, reading is rejected
            if missing_fields != []:
                raise ValueError(f"Missing these fields: {missing_fields}")

            if not isinstance(record['sensor_id'], str):
                raise ValueError(f"Missing or invalid sensor_id. Found: {record['sensor_id']}")

            if not min_tempC <= float(record["temperature"]) <= max_tempC:
                invalid_readings.append(record)
                continue

            if not min_pressure <= float(record["pressure"]) <= max_pressure:
                invalid_readings.append(record)
                continue

            if not min_windspeed <= float(record["windspeed"]) <= max_windspeed:
                invalid_readings.append(record)
                continue

            valid_readings.append(record)

if __name__ == "__main__":
    validate_readings(readings_data)
"""
Read CSV data, normalize records, and group by sensor ID.

Input: .csv data file.
Output: individual sensor .txt files.
"""

import csv
import json
from pathlib import Path

def ingest(filepath):
    """Validates the file type and calls the appropriate ingestion function."""
    try:
        if Path(filepath).suffix.lower() == ".csv":
            ingest_csv(filepath)
        else:
            raise ValueError("Unsupported file type.")
    except Exception as e:
        print(f"An error occurred while ingesting the file: {e}")

def ingest_csv(filepath):
    """Ingests CSV records by reformatting each sensor's records into JSONL separately."""
    sensor_readings = {}
    with open(filepath, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            sensor_id = row.get("sensor_id")
            if sensor_id:
                sensor_readings.setdefault(sensor_id, []).append(row)

    for sensor_id, readings in sensor_readings.items():
        with open(f"data\\output\\{sensor_id}.jsonl", mode="w", encoding="utf-8") as sensor_file:
            for reading in readings:
                sensor_file.write(json.dumps(reading) + "\n")
'''
# debugging
if __name__ == "__main__":
    ingest("data\\input\\readings.csv")
'''
"""
Read CSV data, normalize records, and group by sensor ID.

Input: .csv data file
Output: individual sensor .txt files
"""

import csv
import json

def ingest(filepath, file_type):
    """Validates the file type and calls the appropriate reading function."""
    try:
        if file_type == "csv":
            ingest_csv(filepath)
        else:
            raise ValueError("Unsupported file type. Please use 'csv' or 'jsonl'.")
    except Exception as e:
        print(f"An error occurred while processing the file: {e}")

def ingest_csv(filepath):
    """Reads CSV records and writes them to one JSONL file per sensor ID."""
    with open(filepath, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        sensor_readings = {}

        for row in reader:
            sensor_id = row.get("sensor_id")
            if sensor_id:
                sensor_readings.setdefault(sensor_id, []).append(row)

    for sensor_id, readings in sensor_readings.items():
        with open(f"data\\output\\{sensor_id}.jsonl", mode="w", encoding="utf-8") as sensor_file:
            for reading in readings:
                sensor_file.write(json.dumps(reading) + "\n")

'''
if __name__ == "__main__":
    ingest("data\\input\\readings.csv", "csv")
'''
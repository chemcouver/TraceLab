"""
Read CSV data, normalize records, and group by sensor ID.

Input: .csv data file
Output: individual sensor .txt files
"""

import csv
import json
import datetime as dt

def validate_file(filepath, file_type):
    """Validates the file type and calls the appropriate reading function."""
    try:
        if file_type == "csv":
            ingest_csv(filepath)
        # elif file_type == "jsonl":
            # ingest_jsonl(filepath)
        else:
            raise ValueError("Unsupported file type. Please use 'csv' or 'jsonl'.")
    except Exception as e:
        print(f"An error occurred while processing the file: {e}")

def ingest_csv(filepath):
    """Reads a CSV file and returns a"""
    with open(filepath, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            sensor = row.get("sensor_id")
            for sensor_id in reader:
                sensor_id = row.get("sensor_id")
                if sensor_id == sensor:
                    with open(f"{sensor_id}.txt", mode="a", encoding="utf-8") as sensor_file:
                        reading = [row.get("timestamp"), row.get("temperature"), row.get("pressure"), row.get("windspeed")]
                        sensor_file.write(reading + ", " + "\n")

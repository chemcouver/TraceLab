"""
Read CSV data, normalize records, and group by sensor ID.

Input: .csv data file
Output: individual sensor .txt files
"""

import csv
import json
import datetime as dt

def ingest(filepath, file_type):
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
    """
    Reads a CSV file, processes each row, and writes readings to individual sensor .txt files.
    """
    with open(filepath, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)  # skip header row
        rows = list(reader)  # allow multiple iterations
        processed_sensor_ids = set()  # Track processed sensor IDs to avoid duplicates

        for row in rows:
            sensor_id_i = row[0]

            if sensor_id_i in processed_sensor_ids:
                continue

            for sensor_id_j in rows:
                if sensor_id_j[0] == sensor_id_i:
                    with open(f"data\\output\\{sensor_id_i}.txt", mode="a", encoding="utf-8") as sensor_file:
                        reading = [sensor_id_j[1], sensor_id_j[2], sensor_id_j[3], sensor_id_j[4]]
                        sensor_file.write(", ".join(reading) + "\n")
                        
            processed_sensor_ids.add(sensor_id_i)

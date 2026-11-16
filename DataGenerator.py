"""
This program generates example data in .csv and .jsonl file formats. 

It will be used in TraceLab to demonstrate the ingestion, validation, and analysis of sensor readings.

Datasets will be generated with the following fields:
- timestamp: Datetime
- sensor_id: String
- temperature: Float
- humidity: Float
The generated data is written to a new output file in the chosen format.
"""

import csv
import json
import random
import datetime as dt

fields = ["timestamp", "sensor_id", "temperature", "humidity", "pressure"]

def generate_jsonl_data(records, output_file):
    """Generates random sensor readings"""
    with open(output_file, mode="w", encoding="utf-8") as f:
        for _ in range(1, records):
            data = {
                "timestamp": random_date(dt.datetime(2026, 11, 1), dt.datetime(2026, 11, 4)).isoformat(),
                "sensor_id": f"sensor_{random.randint(1, 10)}",
                "temperature": round(random.uniform(-60.0, 120.0), 2),
                "humidity": round(random.uniform(0.0, 100.0), 2),
                "pressure": round(random.uniform(1000.0, 1100.0), 2)
            }
            f.write(json.dumps(data) + "\n")

def generate_csv_data(records, output_file):
    """Generates random sensor readings"""
    with open(output_file, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(fields) # Initial columns

        for _ in range(1, records):
            writer.writerow([
                random_date(dt.datetime(2026, 11, 1), dt.datetime(2026, 11, 4)).isoformat(),
                f"sensor_{random.randint(1, 10)}",
                round(random.uniform(-60.0, 120.0), 2),
                round(random.uniform(0.0, 100.0), 2),
                round(random.uniform(1000.0, 1100.0), 2)
            ])

def random_date(start, end):
    """Generates random dates between a start and end"""
    return start + dt.timedelta(
        seconds = random.randint(0, int((end - start).total_seconds())),
    )

if __name__ == "__main__":
    generate_csv_data(20, "readings.csv")
    generate_jsonl_data(20, "readings.jsonl")
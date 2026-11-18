"""
This program generates example data in the .csv format. 

It will be used in TraceLab to demonstrate the ingestion, validation, and analysis of sensor readings.

Datasets will be generated with the following fields:
- sensor_id: String
- timestamp: Datetime
- temperature: Float
- pressure: Float
- windspeed: Float

The generated data is written to a new output file in the chosen format.
"""

import csv
import json
import random
import datetime as dt

fields = ["sensor_id", "timestamp", "temperature", "pressure", "windspeed"]

def generate_csv_data(records, output_file):
    """Generates random sensor readings in a CSV file"""
    with open(output_file, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(fields) # Initial header row

        for _ in range(1, records):
            writer.writerow([
                round(random.randint(1, 10)),  # sensor_id
                random_date(dt.datetime(2026, 11, 1, 10, 0, 0), dt.datetime(2026, 11, 1, 20, 0, 0)).isoformat(), # timestamp between 10:00:00 and 20:00:00
                round(random.uniform(-60.0, 120.0), 2), # temperature
                round(random.uniform(100.0, 1200.0), 2), # pressure
                round(random.uniform(0.0, 100.0), 2) # windspeed
            ])

def random_date(start, end):
    """Generates random dates between a start and end"""
    return start + dt.timedelta(
        seconds = random.randint(0, int((end - start).total_seconds())),
    )

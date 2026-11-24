"""
Statistical analysis for the readings

Input: Valid/invalid readings.
Output: Statistical summary for both the valid and invalid readings.
"""

from pathlib import Path
import json
import numpy as np

data_folder = Path("data") / "output" / "validated"

def analyze():
    valid_readings = []
    invalid_readings = []

    for filename, readings in (
        ("valid_readings.jsonl", valid_readings),
        ("invalid_readings.jsonl", invalid_readings)
    ):
        with open(data_folder / filename, "r", encoding="utf-8") as file:
            for line in file:
                if line.strip():
                    readings.append(json.loads(line))

    sensor_ids = sorted({record["sensor_id"] for record in valid_readings}, key=int)

    for sensor_id in sensor_ids:
        readings = [
            r for r in valid_readings
            if r["sensor_id"] == sensor_id
        ]

        print(f"\nSensor {sensor_id}")

        for field in ("temperature", "pressure", "windspeed"):
            values = [float(r[field]) for r in readings]

            print(f"{field}:")
            print(f"  Mean: {np.mean(values):.2f}")
            print(f"  Min: {np.min(values):.2f}")
            print(f"  Max: {np.max(values):.2f}")
            print(f"  Std Dev: {np.std(values):.2f}")

        invalid_count = sum(
            1 for r in invalid_readings
            if r.get("sensor_id") == sensor_id
        )

        print(f"Valid readings: {len(readings)}")
        print(f"Invalid readings: {invalid_count}")
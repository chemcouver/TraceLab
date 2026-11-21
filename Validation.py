"""
Detect valid, invalid, or suspicious readings, and clean them.

Input: Individual sensor .txt files.
Output: Validated and cleaned data, and an invalid readings file.
"""

from pathlib import Path
import datetime as dt
import json

raw_readings_data = Path("data") / "output"

validated_readings_data = Path("data") / "output" / "validated"
validated_readings_data.mkdir(parents=True, exist_ok=True)

cleaned_data = Path("data") / "output" / "cleaned"
cleaned_data.mkdir(parents=True, exist_ok=True)

required_fields = ["sensor_id", "timestamp", "temperature", "pressure", "windspeed"]

# Maximum allowed values
max_tempC = 40
max_pressure = 1100
max_windspeed = 40

# Minimum allowed values
min_tempC = -60
min_pressure = 100
min_windspeed = 0

def validate():
    """Validates the file type and calls the appropriate validation function."""
    for reading in raw_readings_data.iterdir():
        try:
            if reading.suffix.lower() == ".jsonl":
                validate_readings_jsonl(reading)
            else:
                raise ValueError(f"Unsupported file type: {reading}")
        except Exception as e:
            # Suppress exceptions for folders
            if (reading == validated_readings_data):
                continue
            else:
                print(f"An error occurred while validating the file: {e}")

def validate_readings_jsonl(reading):
    reading = Path(reading)

    valid_readings = []
    invalid_readings = []

    with open(reading, mode="r", encoding="utf-8") as reading:
        # Detect any invalid readings
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

        output = (("valid_readings.jsonl", valid_readings), ("invalid_readings.jsonl", invalid_readings))

        for file, readings in output:
            with open(validated_readings_data / file, mode="a", encoding="utf-8") as output_file:
                for record in readings:
                    output_file.write(json.dumps(record) + "\n")

def clean():
    """
    Sort valid and invalid readings in place by sensor ID and timestamp.
    """
    # Normalize timestamps for chronological comparison.
    def sort_key(record):
        sensor_id = record["sensor_id"]

        # Numeric sorting for IDs such as 1, 2, 10.
        try:
            sensor_key = (0, int(sensor_id), sensor_id)
        except ValueError:
            sensor_key = (1, sensor_id, "")

        timestamp = dt.datetime.fromisoformat(record["timestamp"])

        # Treat naive timestamps as UTC for consistent sorting.
        if timestamp.tzinfo is None:
            timestamp = timestamp.replace(tzinfo=dt.timezone.utc)

        timestamp = timestamp.astimezone(dt.timezone.utc)
        return (sensor_key, timestamp)

    for filename in ("valid_readings.jsonl", "invalid_readings.jsonl"):
        validated_file = validated_readings_data / filename
        if not validated_file.exists():
            continue

        with open(validated_file, mode="r", encoding="utf-8") as file:
            readings = [json.loads(line) for line in file if line.strip()]

        readings.sort(key=sort_key)

        with open(validated_file, mode="w", encoding="utf-8") as file:
            for record in readings:
                file.write(json.dumps(record) + "\n")

'''
# debugging
if __name__ == "__main__":
    clean()
'''
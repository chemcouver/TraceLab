"""
Handles ingestion of data from .csv and .jsonl files.

The datasets from either file type should include these fields:
- timestamp: Datetime
- sensor_id: String
- temperature: Float
- humidity: Float
- pressure: Float

Expected input:
- .csv file: A standard CSV file with headers in the first row.
- .jsonl file: A JSON Lines file where each line is a valid JSON object

Expected output:
- For .csv files: Each row will be converted to a dictionary and printed to the
- For .jsonl files: Each line will be parsed as a JSON object and printed to the console.
"""

import csv
import json

def read_csv(filepath):
    """Reads a CSV file and returns a list of dictionaries."""
    with open(filepath, mode="r", newline="", encoding="utf-8") as file:
        # DictReader uses the first row as dictionary keys
        reader = csv.DictReader(file)
        for row in reader:
            # print(dict(row))
            with open("result.txt", "a", encoding="utf-8") as file:
                file.write(str(dict(row)) + "\n")
        print("CSV file read successfully, with data written to result.txt")

def read_jsonl(filepath):
    """Reads a JSONL file line by line."""
    with open(filepath, mode="r", encoding="utf-8") as file:
        for line in file:
            # Skip empty lines
            if line.strip():
                record = json.loads(line)
                print(record)

def validate_file(filepath, file_type):
    """Validates the file type and calls the appropriate reading function."""
    try:
        if file_type == "csv":
            read_csv(filepath)
        elif file_type == "jsonl":
            read_jsonl(filepath)
        else:
            raise ValueError("Unsupported file type. Please use 'csv' or 'jsonl'.")
    except Exception as e:
        print(f"An error occurred while processing the file: {e}")

# demonstrate usage
if __name__ == "__main__":
    # Example usage
    validate_file("readings.csv", "csv")
    # validate_file("data.jsonl", "jsonl")
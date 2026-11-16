"""
Read CSV/JSONL data, normalize records, and group by sensor ID.

Input: .csv or .jsonl data files
Output: individual sensor .txt files
"""

import csv
import json

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

def read_csv(filepath):
    """Reads a CSV file and returns a list of dictionaries."""
    with open(filepath, mode="r", newline="", encoding="utf-8") as file:
        # DictReader uses the first row as dictionary keys
        reader = csv.DictReader(file)
        for row in reader:
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
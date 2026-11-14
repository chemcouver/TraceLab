# Read CSV and JSONL files.

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

# Example usage
if __name__ == "__main__":
    print("--- Reading CSV ---")
    read_csv("data\Awada_final_data.csv")

    # print("\n--- Reading JSONL ---")
    # read_jsonl("data.jsonl")
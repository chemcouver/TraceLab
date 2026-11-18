"""
Test the data generator and ingestion scripts.
"""

from DataGenerator import generate_csv_data
from Ingestion import ingest
from Validation import validate

generate_csv_data(50, "data\\input\\readings.csv")
ingest("data\\input\\readings.csv")
validate()
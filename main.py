"""
Test the data generator and ingestion scripts.
"""

from DataGenerator import generate_csv_data
from Ingestion import ingest
from Validation import validate, clean

generate_csv_data(100, "data\\input\\readings.csv")
ingest("data\\input\\readings.csv")
validate()
clean()
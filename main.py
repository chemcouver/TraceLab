"""
Test the data generator and ingestion scripts.
"""

from DataGenerator import generate_csv_data
from ingestion import ingest_csv

generate_csv_data(20, "data\\output\\readings.csv")
ingest_csv("data\\output\\readings.csv")
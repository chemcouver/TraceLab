"""
Test the data generator and ingestion scripts.
"""

from DataGenerator import generate_csv_data
from Ingestion import ingest_csv

generate_csv_data(20, "data\\input\\readings.csv")
ingest_csv("data\\input\\readings.csv")
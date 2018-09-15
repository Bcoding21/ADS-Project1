import matplotlib.pyplot as plt
import extract, statistics, csv

DATA_FILE = "data.txt"
OUTPUT_FILE = "processed_data.csv"

def read_data_file(file_name):
    with open(file_name, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        return [row for row in csv_reader]

data = extract.read_file(DATA_FILE)
extract.write_file(data, OUTPUT_FILE)
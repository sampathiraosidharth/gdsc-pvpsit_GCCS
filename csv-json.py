import csv
import datetime
import json

import dateutil.utils


def csv_to_json(input_file, output_file):
    # Initialize an empty list to store the data
    data = []

    # Read the CSV file and populate the data list
    with open(input_file, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)

    # Write the data to a JSON file
    with open(output_file, 'w') as jsonfile:
        json.dump(data, jsonfile, indent=4)

# Replace 'input_file.csv' with the path to your CSV file
input_file = '/Users/sidharthsrao/Downloads/gdsc-pvpsit_GCCS/Prasad V. Potluri Siddhartha Institute Of Technology - Vijayawada [17 May].csv'
# Replace 'output_file.json' with the desired path for your output JSON file
output_file = f'{dateutil.utils.today()}.json'

csv_to_json(input_file, output_file)

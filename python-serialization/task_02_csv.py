#!/usr/bin/python3
import csv
import json

def convert_csv_to_json(csv_filename):
    """Converts data from a CSV file to JSON format and writes it to data.json."""
    try:
        """Open the CSV file and read the data"""
        with open(csv_filename, 'r', newline='') as csv_file:
            """Use DictReader to convert each row into a dictionary"""
            csv_reader = csv.DictReader(csv_file)
            data = list(csv_reader)
        
        """Serialize the list of dictionaries to JSON"""
        json_data = json.dumps(data, indent=4)
        
        """Write the serialized JSON data to data.json"""
        with open('data.json', 'w') as json_file:
            json_file.write(json_data)
        
        """Return True if conversion was successful"""
        return True
    
    except FileNotFoundError:
        """Handle file not found exception"""
        print("File not found.")
        return False

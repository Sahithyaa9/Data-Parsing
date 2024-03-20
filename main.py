import sys
import csv
import json
import xml.etree.ElementTree as ET

def read_tab_delimited_file(filename):
    with open(filename, 'r') as file:
        data = [line.strip().split('\t') for line in file]
        header = data[0]
        data = [dict(zip(header, row)) for row in data[1:]]
    return data, header

def convert_to_csv(data, header, output_filename):
    with open(output_filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=header)
        writer.writeheader()
        writer.writerows(data)

def convert_to_json(data, output_filename):
    with open(output_filename, 'w') as jsonfile:
        json.dump(data, jsonfile, indent=4)

def convert_to_xml(data, output_filename):
    root = ET.Element("data")
    for entry in data:
        record = ET.SubElement(root, "record")
        for key, value in entry.items():
            field = ET.SubElement(record, key)
            field.text = value
    tree = ET.ElementTree(root)
    tree.write(output_filename)

if __name__ == "__main__":
    filename = "NFL Offensive Player stats, 1999-2013.txt"

    data, header = read_tab_delimited_file(filename)

    for i, arg in enumerate(sys.argv):
        if arg == "-c":
            convert_to_csv(data, header, "output.csv")
        elif arg == "-j":
            convert_to_json(data, "output.json")
        elif arg == "-x":
            convert_to_xml(data, "output.xml")

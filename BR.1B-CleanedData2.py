#Program cleans the date column and writes only rows that have correct date format
import csv
from datetime import datetime


# Input and output file names
input_file = 'cleaned.csv'
output_file = 'cleaned2.csv'

# Function to check if a row contains invalid date
def is_valid_date(date_str):
    try:
        datetime.strptime(date_str, "%d/%m/%Y")  # Adjust format as needed
        return True
    except ValueError:
        return False

# Open the input file and process the rows
with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
    csv_reader = csv.reader(infile)
    csv_writer = csv.writer(outfile)
    
    # Write the header to the output file
    header = next(csv_reader)
    csv_writer.writerow(header)
    date_index = header.index("date")

    # Process each row
    for row in csv_reader:
        if is_valid_date(row[date_index]):
            csv_writer.writerow(row)
print(f"Cleaned DATE data has been written to {output_file}")

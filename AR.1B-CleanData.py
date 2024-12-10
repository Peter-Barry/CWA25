import csv

# Input and output file names
input_file = 'large.csv'
output_file = 'cleaned.csv'

# Function to check if a row contains spaces or asterisks
def contains_invalid_characters(row):
    for cell in row:
        if ' ' in cell or '*' in cell:
            return True
    return False

# Open the input file and process the rows
with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
    csv_reader = csv.reader(infile)
    csv_writer = csv.writer(outfile)
    
    # Write the header to the output file
    header = next(csv_reader)
    csv_writer.writerow(header)
    
    # Process each row
    for row in csv_reader:
        if not contains_invalid_characters(row):
            csv_writer.writerow(row)

print(f"Cleaned data has been written to {output_file}")

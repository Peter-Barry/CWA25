import csv

# Input and output file names
input_file = 'Large.csv'
output_file = 'SampleData.csv' #Extracted from large.csv

# Open the input file and create a writer for the output file
with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
    csv_reader = csv.reader(infile)
    csv_writer = csv.writer(outfile)

    # Write the header (assuming the first row is the header)
    header = next(csv_reader)
    csv_writer.writerow(header)
    
    # Write every 10th row
    for idx, row in enumerate(csv_reader, start=1):
        if idx % 10 == 0:
            csv_writer.writerow(row)

print(f"Every 10th row has been written to {output_file}")
"""
Explanation:
Input File: large.csv is the source file containing the data.
Output File: CleanData.csv is where the extracted rows are saved.
Header Handling: The first row (header) is written to the output file before processing the rows.
Row Selection: The enumerate function is used to track the row index. Rows where idx % 100 == 0 are written to the output file.
Efficient Processing: The script processes the file line-by-line, ensuring it handles large files without consuming excessive memory.
This code ensures only every 100th row, along with the header, is saved to the new CSV file.
"""








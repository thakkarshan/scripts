
# this file extracts the city name from a string. 
# Eg. Input of "Remote in Toronto, ON" will result in "Toronto" and "ON" added to seprate columns and rest of string discarded.

import csv

# Open the input CSV file and create a new output file
with open('input.csv', 'r+') as input_file, open('output.csv', 'w', newline='') as output_file:
    # Create a CSV reader and writer objects
    reader = csv.reader(input_file)
    writer = csv.writer(output_file)

    # Loop through each row in the input file
    for row in reader:
        
        # Get the value of column 5, this is the column where the string is located
        col5_value = row[5]

        # Split the value by comma
        if "," in col5_value:
            col5_parts = col5_value.split(',')
            last_space_index = col5_parts[0].rfind(" ")
            city = col5_parts[0][last_space_index+1:]
            row[5] = city
            province = col5_parts[1]
            row.append(col5_parts[1])
        else:
            city = col5_value
            remote_province = "Remote"
            row.append(remote_province)

        # Write the modified row to the output file
        writer.writerow(row)
    print('DONE')

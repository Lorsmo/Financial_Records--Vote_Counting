# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

budget_csvpath = os.path.join('Resources', 'budget_data.csv')

# Read in the CSV file
with open(budget_csvpath, newline='') as csvfile:

    # Split the data on commas
    csv_reader = csv.reader(csvfile, delimiter=',')

    header = next(csv_reader)
  
    counter_row = 0
    total = 0
    # Loop through the data
    for row in csv_reader:

    #for row in csv_reader:
        counter_row +=1
        total += int(row[1])
    print("Total Months: " + str(counter_row))
    print("Total: $" + str(total))


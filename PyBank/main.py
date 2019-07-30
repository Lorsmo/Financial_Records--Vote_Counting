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
    first_data, last_data = [], []
    profit_losses = []
    month = []
    # Loop through the data
    for row in csv_reader:
        
        counter_row +=1

        if counter_row == 1:
            first_data = int(row[1])

        if counter_row == counter_row:
            last_data = int(row[1])

        
        profit_losses.append(int(row[1]))
        month.append(str(row[0]))
    average_change = round(((last_data - first_data) / (counter_row - 1)), 2)
    
    print("Financial Analysis")
    print("----------------------------")

    print("Total Months: " + str(len(month)))
    print("Total: $" + str(sum(profit_losses)))
    print("Average Changes: $" + str(average_change))
    print("Greatest Increase in Profits: " + str(max(profit_losses)))
    print("Greatest Decrease in Profits: " + str(min(profit_losses)))
    
    #print("Greteast: " + str(max(profit_losses) + str(max(month))))
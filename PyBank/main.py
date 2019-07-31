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
    Imont = 0
    # Loop through the data
    for row in csv_reader:
        
        counter_row +=1

        if counter_row == 1:
            first_data = int(row[1])

        if counter_row == counter_row:
            last_data = int(row[1])

        
        #profit_losses.append(int(row[1]))
        #p = int(row[1])
        #if p == max(str(profit_losses)):
            #Imonth = row[0]

        profit_losses.append(int(row[1]))
        month.append(str(row[0]))
        
        
    average_change = round(((last_data - first_data) / (counter_row - 1)), 2)
 

    print("Financial Analysis")
    print("----------------------------")

    print(f"Total Months: {len(month)}")
    print(f"Total: ${sum(profit_losses)}")
    print(f"Average Changes: ${average_change}")
    print(f"Greatest Increase in Profits: {month[profit_losses.index(max(profit_losses))]}  (${max(profit_losses)})")
    print(f"Greatest Decrease in Profits: {month[profit_losses.index(min(profit_losses))]}  (${min(profit_losses)})")
    
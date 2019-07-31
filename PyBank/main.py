# Import the os module to create file paths across operating systems
import os

# Module for reading CSV files
import csv

# Set path for file
budget_csvpath = os.path.join('Resources', 'budget_data.csv')

# Open and read in the CSV file
with open(budget_csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter (split the data on commas), and variable that holds contents
    csv_reader = csv.reader(csvfile, delimiter=',')
    
    # Read the header row first
    header = next(csv_reader)
    
    profit_losses = []
    month = []

    # Loop through the data
    for row in csv_reader:

        profit_losses.append(int(row[1]))
        
        month.append(str(row[0]))
 
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {len(month)}")
    print(f"Total: ${sum(profit_losses)}")
    print(f"Average Changes: ${round(((profit_losses[len(month)-1] - profit_losses[0]) / (len(month) - 1)), 2)}")
    print(f"Greatest Increase in Profits: {month[profit_losses.index(max(profit_losses))]}  (${max(profit_losses)})")
    print(f"Greatest Decrease in Profits: {month[profit_losses.index(min(profit_losses))]}  (${min(profit_losses)})")

# Specify the file to write to
# output_path = os.path.join("Analysis", "Financial_Analysis")

# Open the file using "write" mode. Specify the variable to hold the contents
# with open(output_path, "w") as text_file:
 #   print(def print_analysis)
  #  txtwriter = csv.writer(text_file)
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
    
    # Lists to store data
    profit_losses = []
    month = []

    # Loop through the data
    for row in csv_reader:

        # Add the profit and losses
        profit_losses.append(int(row[1]))
        
        # Add the months
        month.append(str(row[0]))
    
    # print the results in the terminal
    print("---------------------------------------------")
    print(F"Financial Analysis from {month[0]} to {month[len(month)-1]}")
    print("---------------------------------------------")
    print(f"Total Months: {len(month)}")
    print(f"Total: ${sum(profit_losses)}")
    print(f"Average Changes: ${round(((profit_losses[len(month)-1] - profit_losses[0]) / (len(month) - 1)), 2)}")
    print(f"Greatest Increase in Profits: {month[profit_losses.index(max(profit_losses))]}  (${max(profit_losses)})")
    print(f"Greatest Decrease in Profits: {month[profit_losses.index(min(profit_losses))]}  (${min(profit_losses)})")
    print("---------------------------------------------")
  
    

#Specify the file to write to
output_path = os.path.join("Analysis", f"Financial_Analysis {month[0]} - {month[len(month)-1]}.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, "w", newline="") as f:
    
    # Print in a text file
    print(("---------------------------------------------"), file =f)
    print((F"Financial Analysis from {month[0]} to {month[len(month)-1]}"), file =f)
    print(("---------------------------------------------"), file =f)
    print((f"Total Months: {len(month)}"), file =f)
    print((f"Total: ${sum(profit_losses)}"), file =f)
    print((f"Average Changes: ${round(((profit_losses[len(month)-1] - profit_losses[0]) / (len(month) - 1)), 2)}"), file =f)
    print((f"Greatest Increase in Profits: {month[profit_losses.index(max(profit_losses))]}  (${max(profit_losses)})"), file =f)
    print((f"Greatest Decrease in Profits: {month[profit_losses.index(min(profit_losses))]}  (${min(profit_losses)})"), file =f)
    print(("---------------------------------------------"), file =f)

    

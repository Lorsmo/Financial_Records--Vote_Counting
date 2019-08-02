# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

# Set path for file
election_csvpath = os.path.join('Resources', 'election_data.csv')

# Open and read in the CSV file
with open(election_csvpath, newline='') as csvfile:

    # Split the data on commas
    csv_reader = csv.reader(csvfile, delimiter=',')

    # Read the header row first
    header = next(csv_reader)

    # Lists to store data
    candidat_list = []
    votes = []
    
    # Loop through the data
    for row in csv_reader:
        
        # Add each votes to the list "votes"
        votes.append(str(row[2]))
        
        # If the vote is for a candidate not present in the candidate list
        if str(row[2]) not in candidat_list:

            # Put the candidate's name in the candidate list
            candidat_list.append(str(row[2]))

# Print the election results       
print("-----------------------")  
print("Election Results")
print("-----------------------")
print(f"Total Votes: {len(votes)}")
print("-----------------------")
for i in range (len(candidat_list)):
    print(f"{candidat_list[i]}: {round((votes.count(candidat_list[i]))/len(votes)*100, 3)}% ({votes.count(candidat_list[i])})")
    if votes.count(candidat_list[i]) > votes.count(candidat_list[i-1]):
        winner = candidat_list[i]
print("-----------------------")
print(f"Winner: {winner}")
print("-----------------------")

#Specify the file to write to
output_path = os.path.join("Election_Results", f"Election Results {candidat_list}.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, "w", newline="") as f:
    
    # Print in a text file
    print(("-----------------------"), file =f) 
    print(("Election Results"), file =f)
    print(("-----------------------"), file =f)
    print((f"Total Votes: {len(votes)}"), file =f)
    print(("-----------------------"), file =f)
    for i in range (len(candidat_list)):
        print((f"{candidat_list[i]}: {round((votes.count(candidat_list[i]))/len(votes)*100, 3)}% ({votes.count(candidat_list[i])})"), file =f)
        if votes.count(candidat_list[i]) > votes.count(candidat_list[i-1]):
            winner = candidat_list[i]
    print(("-----------------------"), file =f)
    print((f"Winner: {winner}"), file =f)
    print(("-----------------------"), file =f)

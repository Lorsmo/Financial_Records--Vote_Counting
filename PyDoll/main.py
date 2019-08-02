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
    candidate_list = []
    votes = []
    
    # Loop through the data
    for row in csv_reader:
        
        # Add each votes to the list "votes"
        votes.append(str(row[2]))

        # Variable total_votes equal to lenght of column vote
        total_votes = len(votes)
        
        # If the vote is for a candidate not present in the candidate list
        if str(row[2]) not in candidate_list:

            # Put the candidate's name in the candidate list
            candidate_list.append(str(row[2]))

# Print the election results       
print("-----------------------")  
print("Election Results")
print("-----------------------")
print(f"Total Votes: {total_votes}")
print("-----------------------")

# Loop through the candidates into the list
for i in range (len(candidate_list)):
    
    # For readability, assign values to variables with descriptive names
    candidate = candidate_list[i]        
    votes_count = votes.count(candidate_list[i])
    previous_votes_count = votes.count(candidate_list[i-1])
    percentage_votes = round((votes_count/total_votes)*100, 3)
    
    # print the results for each candidate
    print(f"{candidate}: {percentage_votes}% ({votes_count})")
    
    # If number of votes for the currently candidate is greater than for the previous one, 
    if votes_count > previous_votes_count:

        # the variable winner equal the name of this candidate
        winner = candidate

print("-----------------------")
print(f"Winner: {winner}")
print("-----------------------")

#Specify the file to write to
output_path = os.path.join("Election_Results", f"Election Results {candidate_list}.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, "w", newline="") as f:
    
    # Print in a text file
    print(("-----------------------"), file =f) 
    print(("Election Results"), file =f)
    print(("-----------------------"), file =f)
    print((f"Total Votes: {len(votes)}"), file =f)
    print(("-----------------------"), file =f)
    for i in range (len(candidate_list)):
        print((f"{candidate_list[i]}: {round((votes.count(candidate_list[i]))/len(votes)*100, 3)}% ({votes.count(candidate_list[i])})"), file =f)
        if votes.count(candidate_list[i]) > votes.count(candidate_list[i-1]):
            winner = candidate_list[i]
    print(("-----------------------"), file =f)
    print((f"Winner: {winner}"), file =f)
    print(("-----------------------"), file =f)

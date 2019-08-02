# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

election_csvpath = os.path.join('Resources', 'election_data.csv')

with open(election_csvpath, newline='') as csvfile:

    # Split the data on commas
    csv_reader = csv.reader(csvfile, delimiter=',')

    header = next(csv_reader)

    candidat_list = []
    votes = []
    
    for row in csv_reader:
        
        votes.append(str(row[2]))
        
        if str(row[2]) not in candidat_list:
            candidat_list.append(str(row[2]))
        
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
print("----------------------")


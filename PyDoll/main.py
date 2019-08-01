# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

election_csvpath = os.path.join('Resources', 'light_election_data.csv')

with open(election_csvpath, newline='') as csvfile:

    # Split the data on commas
    csv_reader = csv.reader(csvfile, delimiter=',')

    header = next(csv_reader)

    candidat_list = []
    candidates = []
    for row in csv_reader:

        candidates.append(row[2])

        for candidate in candidates:
            if candidate not in candidat_list:
                candidat_list.append(candidate)
            
                

    
    print("Election Results")
    print("----------------------")
    print(f"Total Votes: {len(candidates)}")
    print("----------------------")
    for i in range (len(candidat_list)):
        candidates.count(candidat_list[i])
        print(f"{candidat_list[i]}: {candidates.count(candidat_list[i])}")

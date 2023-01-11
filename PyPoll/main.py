
import os
import csv

election_csv = os.path.join("/Users/Justin/Documents/Bootcamp_Home folder/homework/Module 3/python_challenge/PyPoll/Resources/election_data.csv")

total_votes = 0

with open(election_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter= ",")
    csv_header = next(csv_reader)

    total_votes = sum(1 for row in csv_reader)
    csv_file.seek(0)
    csv_reader = csv_file.read()
    CCS = (csv_reader.count("Charles Casper Stockham")/ total_votes)
    DD = (csv_reader.count("Diana DeGette")/ total_votes)
    RAD = (csv_reader.count("Raymon Anthony Doane")/ total_votes)

print("")
print("Election Results")
print( "----------------------------")
print(str(total_votes))
print("----------------------------")
print("Charles Casper Stockham: ", (f"{CCS: .3%}") , (csv_reader.count("Charles Casper Stockham")))
print("Diana DeGette: ",(f"{DD: .3%}") , (csv_reader.count("Diana DeGette")))
print("Raymon Anthony Doane: ", (f"{RAD: .3%}"), (csv_reader.count("Raymon Anthony Doane")))

Results = {"Charles Casper Stockham":CCS, "Diana DeGette":DD, "Raymon Anthony Doane":RAD}
Winner = max(Results, key=Results.get)

print("----------------------------")
print("Winner: ", {Winner})
print("----------------------------")




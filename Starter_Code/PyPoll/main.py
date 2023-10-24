# import modules and csv file
import os
import csv
# set file path
csvpath = os.path.join('Resources', 'election_data.csv')
# open csv reader
with open(csvpath) as electionfile:
    csvreader = csv.reader(electionfile)
    #print(csvreader)

    # read header row
    csv_header = next(csvreader)
    #print(f"Header: {csv_header}")

    # assign values to variables
    total_votes = 0
    candidates = []
    num_votes = []
    percent_votes = []
    
    # loop through all the rows after the header
    for row in csvreader:
        # calculate total votes
        total_votes +=1
        # get the name of the candidates
        if row[2] not in candidates:
            candidates.append(row[2])
            index = candidates.index(row[2])
            num_votes.append(1)
        else:
            index = candidates.index(row[2])
            num_votes[index] += 1

    # calculate percentage
    for votes in num_votes:
        percentage = float(votes)/float(total_votes) * 100
        percentage = "%.3f%%" % percentage
        percent_votes.append(percentage)

    # calculate winning candidate results
    winner = max(num_votes)
    index = num_votes.index(winner)
    winning_candidate = candidates[index]

# specify the file to write to
output_file = os.path.join("Analysis", "results.txt")
# open the file using write mode
with open(output_file, 'w') as file:
    file.write("Election Results")
    file.write("\n")
    file.write("----------------------")
    file.write("\n")
    file.write(f"Total Votes: {total_votes}")
    file.write("\n")
    file.write("-----------------------")
    file.write("\n")
    for i in range(len(candidates)):
        file.write(f"{candidates[i]}: {str(percent_votes[i])} ({str(num_votes[i])}) \n")
    file.write("-----------------------")
    file.write("\n")
    file.write(f"Winner: {winning_candidate}")
    file.write("\n")
    file.write("-----------------------")

# print the results
print("Election Results")
print("-----------------------")
print(f"Total Votes: {total_votes}")
print("-----------------------")
for i in range(len(candidates)):
    print(f"{candidates[i]}: {str(percent_votes[i])} ({str(num_votes[i])})")
print("-----------------------")
print(f"Winner: {winning_candidate}")
print("-----------------------")
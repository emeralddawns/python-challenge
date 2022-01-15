 # * The total number of votes cast

 # * A complete list of candidates who received votes

 # * The percentage of votes each candidate won

 # * The total number of votes each candidate won

 # * The winner of the election based on popular vote.

#import useful functions
import os
import csv

#paths for reading and writing data
csvpath = os.path.join('Resources', 'election_data.csv')
output_path = os.path.join("Analysis", "Election_Results.txt")

#initialize values
votes = 0
candidates = []
vote_count = []
# percentage = []
i=int(0)
j=int(0)

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read/store the header row first, next consumes a row (to get past the header)
    csv_header = next(csvreader)

    # Read each row of data after the header, make calculations, and store values
    for row in csvreader:
        votes += 1                          #count the total number of votes

        if row[2] not in candidates:        
            candidates.append(row[2])       #create list of unique candidates
            vote_count.append(int(1))       #create list of vote counts for unique candidates
        else:
            i = 0    
            for name in candidates:
                if name == row[2]:
                    vote_count[i] += 1      # +1 to a vote count for a unique candidate
                i += 1

    percent_vote = [(x / votes) for x in vote_count]      #calculate the percentage of votes received

    print(f"{candidates}")
    print(f"{vote_count}")
    print(f"{percent_vote}")
#summarize the data in one place so that the terminal and output .txt receive the same information
line = (f"-------------------------")
summary_header = [(f"Election Results"),
            (line),
            (f"Total Votes: {votes}"),
            (line),]

#for names in candidates:
#    percent_vote[j] = "{:.3%}".format(percent_vote[j])
#    print(f"{candidates[j]}: {percent_vote[j]} ({vote_count[j]})")
#    j+=1

#print to the terminal
for line in summary_header:
    print(line)

for names in candidates:
    percent_vote[j] = "{:.3%}".format(percent_vote[j])
    print(f"{candidates[j]}: {percent_vote[j]} ({vote_count[j]})")
    j+=1

#print to the .txt file
with open(output_path, "w", newline = '') as datafile:
    writer = csv.writer(datafile)
    for line in summary_header:
        writer.writerow([line])

    j = int(0)
    for names in candidates:
#        percent_vote[j] = "{:.0%}".format(percent_vote[j])
        writer.writerow([f"{candidates[j]}: {percent_vote[j]} ({vote_count[j]})"])
        j += 1

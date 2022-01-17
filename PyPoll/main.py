 #This code currently calculates the following:
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
print_line = []

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
            print_line.append(0)            #create a proper sized print_line list for output purposes
        else:
            i = 0    
            for name in candidates:
                if name == row[2]:
                    vote_count[i] += 1      # +1 to a vote count for a unique candidate
                i += 1

    percent_vote = [(x / votes) for x in vote_count]      #calculate the percentage of votes received
    percent_vote = ["{:.3%}".format(x) for x in percent_vote]   #format the percentage values

    max_votes = max(vote_count)             #find max votes
    winner_index = vote_count.index(max_votes)  #find index for max votes
    winner = candidates[winner_index]       #use index to find name of winner

#summarize the data in one place so that the terminal and output .txt receive the same information
dashes = (f"-------------------------")
summary_header = [(f"Election Results"),
            (dashes),
            (f"Total Votes: {votes}"),
            (dashes),]

j=int(0)        #create the "Candidate: Votes% (Vote Count)" lines
for names in candidates:
    print_line[j] = f"{candidates[j]}: {percent_vote[j]} ({vote_count[j]})"
    j+=1

summary_winner = [(dashes),
                    (f"Winner: {winner}"),
                    (dashes)]


#print to the terminal
for line in summary_header:
    print(line)

print(*print_line, sep="\n")

for line in summary_winner:
    print(line)


#print to the .txt file
with open(output_path, "w", newline = '') as datafile:
    writer = csv.writer(datafile, delimiter = '\n')
    for line in summary_header:
        writer.writerow([line])

    writer.writerow(print_line)

    for line in summary_winner:
        writer.writerow([line])
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

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read/store the header row first, next consumes a row (to get past the header)
    csv_header = next(csvreader)

    # Read each row of data after the header, make calculations, and store values
    for row in csvreader:
        votes += 1


#summarize the data in one place so that the terminal and output .txt receive the same information
line = (f"-------------------------")
summary = [(f"Election Results"),
            (line),
            (f"Total Votes: {votes}"),
            (line),]

#print to the terminal
for line in summary:
    print(line)

#print to the .txt file
with open(output_path, "w", newline = '') as datafile:
    writer = csv.writer(datafile)
    for line in summary:
        writer.writerow([line])
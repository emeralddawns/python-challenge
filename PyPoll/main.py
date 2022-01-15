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

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read/store the header row first, next consumes a row (to get past the header)
    csv_header = next(csvreader)

    # Read each row of data after the header, make calculations, and store values
    for row in csvreader:

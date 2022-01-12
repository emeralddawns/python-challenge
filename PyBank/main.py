#* Your task is to create a Python script that analyzes the records to calculate each of the following:

#  * The total number of months included in the dataset

#  * The net total amount of "Profit/Losses" over the entire period

#  * Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes

#  * The greatest increase in profits (date and amount) over the entire period

#  * The greatest decrease in profits (date and amount) over the entire period

import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

print("here are some words")
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader) #next consumes a row
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        print(row)
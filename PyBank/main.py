#* Your task is to create a Python script that analyzes the records to calculate each of the following:

#  * The total number of months included in the dataset

#  * The net total amount of "Profit/Losses" over the entire period

#  * Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes

#  * The greatest increase in profits (date and amount) over the entire period

#  * The greatest decrease in profits (date and amount) over the entire period

import os
import csv
import sys

csvpath = os.path.join('Resources', 'budget_data.csv')
output_path = os.path.join("Analysis", "Financial_Analysis.txt")

net = 0
months = 0
month_change = []
max_inc = 0.0
max_dec = 0.0

# prove it is being read
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    ## print(csvreader)

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader) #next consumes a row
    ## print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:        
        ## print(row)
        months += 1
        net += float(row[1])
        net_dollar = "${:.2f}".format(net)      #"${:,.2f}".format(net) format with commas
        # month_change[row-1] = float()
        if float(row[1]) > max_inc:
            max_inc = float(row[1])
            inc_month = row[0]
        if float(row[1]) < max_dec:
            max_dec = float(row[1])
            dec_month = row[0]

#print to terminal
print(f"Financial Analysis")
print(f"----------------------------")
print(f"Total Months: {months}")
print(f"Net Total Amount: {net_dollar}")
print(f"Average Change: {net_dollar}")
print(f"Greatest Increase in Profits: {inc_month} ({max_inc})")
print(f"Greatest Decrease in Profits: {dec_month} ({max_dec})")


#print to output text file
with open(output_path, "w") as datafile:
    writer = csv.writer(datafile)

    writer.writerow([f"Financial Analysis"])
    writer.writerow([f"----------------------------"])
    writer.writerow([f"Total Months: {months}"])
    writer.writerow([f"Net Total Amount: {net_dollar}"])
    writer.writerow([f"Average Change: {net_dollar}"])
    writer.writerow([f"Greatest Increase in Profits: {inc_month} ({max_inc})"])
    writer.writerow([f"Greatest Decrease in Profits: {dec_month} ({max_dec})"])



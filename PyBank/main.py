#this code currently calculates the following:
    #The total number of months included in the dataset
    #The net total amount of "Profit/Losses" over the entire period
    #The average month-to-month change over the course of the dataset
    #The greatest increase in profits (date and amount) over the entire period
    #The greatest decrease in profits (date and amount) over the entire period

#import useful functions
import os
import csv

#paths for reading and writing data
csvpath = os.path.join('Resources', 'budget_data.csv')
output_path = os.path.join("Analysis", "Financial_Analysis.txt")

#initialize values
net = 0
months = 0
prev_month = "IgnoreFirstRow"
month_change = []
max_inc = 0.0
max_dec = 0.0

def dollarbills(number):        #function for consistently and properly formatting dollar amounts
    if float(number) >= 0:
        return "${:.2f}".format(number)         # $0.00 w/no commas
    else:
        return "-${:.2f}".format(abs(number))   # -$0.00 w/no commas (use the absolute value so there aren't 2 negative signs)

# open the file to read it and use the data for math
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read/store the header row first, next consumes a row (to get past the header)
    csv_header = next(csvreader)

    # Read each row of data after the header, make calculations, and store values
    for row in csvreader:        
        months += 1                         #number of months in dataset
        net += float(row[1])                #net total amount

        if prev_month != "IgnoreFirstRow":  #gather monthly change data, after ignoring the first data row
            change = float(row[1]) - prev_month
            month_change.append(float(change))

        prev_month = float(row[1])          #store data for the "prev_month"

        if float(row[1]) > max_inc:         #finding the max increase and the month it is in
            max_inc = float(row[1])
            inc_month = row[0]
        if float(row[1]) < max_dec:         #finding the max decrease and the month it is in
            max_dec = float(row[1])
            dec_month = row[0]

    average = sum(month_change) / len(month_change) #calculate the average change

#summarize the data in one place so that the terminal and output .txt receive the same information
summary = [(f"Financial Analysis"),
            (f"----------------------------"),
            (f"Total Months: {months}"),
            (f"Net Total Amount: {dollarbills(net)}"),
            (f"Average Change: {dollarbills(average)}"),
            (f"Greatest Increase in Profits: {inc_month} ({dollarbills(max_inc)})"),
            (f"Greatest Decrease in Profits: {dec_month} ({dollarbills(max_dec)})"),
            ]

#print to the terminal
for line in summary:
    print(line)

#print to the .txt file
with open(output_path, "w", newline = '') as datafile:
    writer = csv.writer(datafile)
    for line in summary:
        writer.writerow([line])

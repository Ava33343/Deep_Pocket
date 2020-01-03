## PyBank due Jan 6, 2020

# Import the pathlib and csv library
from pathlib import Path
import csv

# Set the file path
csvfile = open("/Users/ava/OneDrive/github/Resources/Homework_02-Python_Instructions_PyBank_Resources_budget_data.csv", "r")

# Read csv in csvreader
csvreader = csv.reader(csvfile)

# Initialize
next(csvreader) # skip first line for titles
date = []
profits = []
profits_change = []

# Read Date in 1st row as "date" and Profit/Losses in the 2nd row as "profits"
for row in csvreader:
    date.append(row[0])
    profits.append(float(row[1]))
    
# Loop for changes in Profit/Losses of Column 2
for i in range(1,len(profits)):
  profits_change.append(profits[i] - profits[i-1])   
  average_profits_change = sum(profits_change)/len(profits_change)

  max_profits_change = max(profits_change)
  min_profits_change = min(profits_change)

  max_profits_change_date = str(date[profits_change.index(max(profits_change))])
  min_profits_change_date = str(date[profits_change.index(min(profits_change))])
    
print("PyBank Analysis")
print("-----------------------------------")
print("Total Months:", len(date))
print("Net Aggregate Profit/Losses: $", sum(profits))
print("Average Change in Profit/Losses: $", round(average_profits_change, 2))
print("Greatest Increase in Profits:", max_profits_change_date,"($", max_profits_change,")")
print("Greatest Decrease in Losses:", min_profits_change_date,"($", min_profits_change,")")

# Output format for "PyBank Analysis"
header = ["Total Months", "Net Aggregate Profit/Losses $", "Average Change in Profit/Losses $", "Date of Greatest Increase in Profits", "$ Greatest Increase in Profits", "Date of Greatest Decrease in Losses", "$ Greatest Decrease in Losses"]


metrics = [len(date), sum(profits), round(average_profits_change, 2), max_profits_change_date, max_profits_change, min_profits_change_date, min_profits_change]
output_path = Path('/Users/ava/OneDrive/github/python-homework/PyBank/PyBank_Analysis.csv')

# Open the "PyBank Analysis" output path as a file object
with open(output_path, 'w') as csvfile:
    # Set the file object as a csvwriter object
    csvwriter = csv.writer(csvfile, delimiter=',')
    # Write the header to the output file
    csvwriter.writerow(header)
    # Write the list of metrics to the output file
    csvwriter.writerow(metrics)

"""
References:

* "csv_reader.py", UC GitLab Repository 
* https://stackoverflow.com/questions/35350086/argument-1-must-be-an-iterator-what-am-i-doing-wrong
* https://stackoverflow.com/questions/46965192/python-how-can-i-find-difference-between-two-rows-of-same-column-using-loop-in
* https://stackoverflow.com/questions/22282760/filenotfounderror-errno-2-no-such-file-or-directory
* https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files

"""
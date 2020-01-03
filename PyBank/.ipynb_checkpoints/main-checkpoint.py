## PyBank

"""![Revenue](Images/revenue-per-lead.jpg)

In this activity, you are tasked with creating a Python script for analyzing the financial records of your company. You will be provided with a financial dataset in this file: 

[budget_data.csv](PyBank/Resources/budget_data.csv). 

This dataset is composed of two columns, Date and Profit/Losses. (Thankfully, your company has rather lax standards for accounting, so the records are simple.)

Your task is to create a Python script that analyzes the records to calculate each of the following:

* The total number of months included in the dataset.

* The net total amount of Profit/Losses over the entire period.

* The average of the changes in Profit/Losses over the entire period.

* The greatest increase in profits (date and amount) over the entire period.

* The greatest decrease in losses (date and amount) over the entire period.

Your resulting analysis should look similar to the following:

  ```text
  Financial Analysis
  ----------------------------
  Total Months: 86
  Total: $38382578
  Average  Change: $-2315.12
  Greatest Increase in Profits: Feb-2012 ($1926159)
  Greatest Decrease in Profits: Sep-2013 ($-2196167)
  ```

Your final script should print the analysis to the terminal and export a text file with the results."""

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

print("Financial Analysis")
print("-----------------------------------")
print("Total Months:", len(date))
print("Net Aggregate Profit/Losses: $", sum(profits))
print("Average Change in Profit/Losses: $", round(avg_profits_change))
print("Greatest Increase in Profits:", max_rev_change_date,"($", max_profits_change,")")
print("Greatest Decrease in Losses:", min_rev_change_date,"($", min_profits_change,")")

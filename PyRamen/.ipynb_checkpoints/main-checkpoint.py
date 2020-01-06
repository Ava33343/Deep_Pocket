# -*- coding: UTF-8 -*-
"""PyRamen Homework Starter."""

# @TODO: Import libraries
import csv
from pathlib import Path

# @TODO: Set file paths for menu_data.csv and sales_data.csv
with open("../Resources/menu_data.csv", 'r') as menufile:  
    menufile = open("../Resources/menu_data.csv", "r")

# Read csv in csvreader & skip the first line of titles
menu = csv.reader(menufile, delimiter=',')

next(menu)

with open("../Resources/sales_data.csv", 'r') as salesfile:  
    salesfile = open("../Resources/sales_data.csv", "r")

# Read csv in csvreader & skip the first line of titles
    sales = csv.reader(salesfile, delimiter=',')

next(sales)

# Append the column 'Count' to the header
sales_header.append("Count")
# Append the header to the list of sales
sales.append(sales_header)
# Print the new header
print(sales_header)

# @TODO: Initialize list objects to hold our menu and sales data
menu = []
sales = []

# In menu:
items = []
categories = []
descriptions = []
prices = []
costs = []

for row in menu:
    items.append(row[0])
    categories.append(row[1])
    descriptions.append(row[2])
    prices.append(float(row[3]))
    costs.append(float(row[4]))
    
    price = float(row[3])
    cost = float(row[4])
    
    def profit(price, cost):
    profit = price - cost
    return profit

"""
Test Output: 

price = 2
cost = 1

profit = profit(price, cost)
print(f"Profit: {profit}")

output
Profit: 1
"""
    
# @TODO: Initialize dict object to hold our key-value pairs of items and metrics
report = {}

# Initialize a row counter variable
row_count = 0

# In sales:
IDs = []
dates = []
cards = []
quantities = []
sales_item = []

# @TODO: Loop over every row in the sales list object

for row in sales:
   
    IDs.append(row[0])
    dates.append(row[1])
    cards.append(row[2])
    quantities.append(float(row[3]))
    sales_item.append(row[4])
    
    quantity = float(row[3])
    
 # @TODO:
    # If the item value not in the report, add it as a new entry with initialized metrics
    # Naming convention allows the keys to be ordered in logical fashion, count, revenue, cost, profit

count = []
revenue = []
cogs = []
profit = []


# LOGICS:

count = {}

for i, value in enumerate(sales_item):
    if str(value) not in count:
        count[str(value)] = quantities[i]
    else:
        count[str(value)] += quantities[i]
        
for sales_item in sorted(count):
    print('{}, {}'.format(sales_item, count[sales_item]))
    
"""
Output: 
burnt garlic tonkotsu ramen, 9070.0
miso crab ramen, 8890.0
nagomi shoyu, 9132.0
shio ramen, 9180.0
soft-shell miso crab ramen, 9130.0
spicy miso ramen, 9238.0
tonkotsu ramen, 9288.0
tori paitan ramen, 9156.0
truffle butter ramen, 8982.0
vegetarian curry + king trumpet mushroom ramen, 8824.0
vegetarian spicy miso, 9216.0

"""
    

# Create a dictionary report combining menu and sales data
row_count += 1

for i, value in enumerate(sales_item):
    if sales_item in items:
        def count(quantity):
            count += quantity
            return count
        def revenue(price, quantity):
            revenue += price * quantity
            return revenue
        def profit(price, profit):
            profit += price * profit
            return profit


        report = {"01-count":count, "02-revenue":revenue, "03-cogs":cogs, "04-profit":profit}
        print(f"report = {sales_item} {"01-count":{count}, "02-revenue":{revenue}, "03-cogs":{cogs}, "04-profit":{profit}})

    else:
    print('{} does not equal {}! NO MATCH!'.format(items, sales_item))
    
  # Parse and print the file line by line. The print statement adds an
    # extra line break to each line in the output.
    
    # @TODO: Increment the row counter by 1
    for line in report:
        print(f"line {row_counter}: {line}")
    row_counter += 1

header = ["01-count", "02-revenue", "03-cogs", "04-profit"]
metrics = [count, revenue, cogs, profit]

# @TODO: Write out report to a text file (won't appear on the command line output)
# Set the output file path
output_path = Path('../python-homework/PyRamen/PyRamen_Report.txt')

# Open the output_path as a file object in "write" mode ('w')
# Write a header line and write the contents of 'text' to the file
with open(output_path, 'w') as file:
    file.write("This is an output file.\n")
    file.write(text)
    
with open(output_path, 'w') as file:
    # Set the file object as a csvwriter object
    txtwriter = file.writer(file, delimiter=',')
    # Write the header to the output file
    txtwriter.writeline(header)
    # Write the list of metrics to the output file
    txtwriter.writeline(metrics)
    
    
"""
References:

* "csv_reader.py", UC GitLab Repository 
* https://stackoverflow.com/questions/35350086/argument-1-must-be-an-iterator-what-am-i-doing-wrong
* https://stackoverflow.com/questions/46965192/python-how-can-i-find-difference-between-two-rows-of-same-column-using-loop-in
* https://stackoverflow.com/questions/22282760/filenotfounderror-errno-2-no-such-file-or-directory
* https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
* https://www.oreilly.com/library/view/python-cookbook/0596001673/ch01s15.html
* https://www.digitalocean.com/community/tutorials/how-to-convert-data-types-in-python-3
* https://www.geeksforgeeks.org/python-zipping-two-lists-of-lists/
* https://docs.python.org/3/
* https://www.tutorialspoint.com/python/python_dictionary.htm
* https://www.pythonforbeginners.com/dictionary/how-to-use-dictionaries-in-python/

"""
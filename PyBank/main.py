# first i need to read our data to analyse that
import os
import csv

# we want to use our script for all csv file. that's why i give a variable
#that represent our file. so we would just need to change filename
file_name = "budget_data_1.csv"

datapath = os.path.join('raw_data', file_name)


with open(datapath, 'r') as budget_csv:
    budget = csv.reader(budget_csv, delimiter=',')

    next(budget, None)
    totalrev = 0
    monthcounter = 0
    initial_rev = 0
    greatest_inc = 0
    greatest_dec = 0 

    for row in budget:
        dates = row[0]
        revenues = int(row[1])

        totalrev = totalrev + int(revenues)
        monthcounter = monthcounter + 1
        initial_rev = revenues

        if revenues < greatest_dec:
            greatest_dec = revenues
            greatest_dec_info = (str(dates) + " " + str(greatest_dec))
        elif revenues > greatest_inc:
            greatest_inc = revenues
            greatest_inc_info = (str(dates) + " " + str(greatest_inc))
avarage_change = int(totalrev / monthcounter)

print("--------------")
print("Financial Analysis")
print("-------------------------")
print("Total Months : " + str(monthcounter))
print("Total Revenue : " + str(totalrev))
print("Avarage Change : " + str(avarage_change))
print("Greatest increase : " + str(greatest_inc_info))
print("Greatest Decrease : " + str(greatest_dec_info))


  
   



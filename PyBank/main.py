import os
import csv

#Path to collect data from the resources folder
budget_data_csv = os.path.join("..", "Resources", "budget_data.csv")

print(f'                   ')
print(f'Financial Analysis')
print(f'---------------------------')
#open and read csv
with open(budget_data_csv) as csv_file:
    csv_reader = csv.reader(budget_data_csv, delimiter=',')
    csv_header = next(csv_file)
    row_count = len(list(csv_file))
    #profitloss_index = csv_file.index("Profit/Losses") Code Debug
    #profitloss_index = 0 Code Debug
#total = 0 Code Debug
#for row in csv_header: Code
    #total =+ float(row[profitloss_index]) Code Debug
print("Total Months: " + str(row_count))
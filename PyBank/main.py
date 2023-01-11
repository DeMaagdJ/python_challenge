
import os
import csv

#Path to collect data from the resources folder
budget_data_csv = os.path.join("/Users/Justin/Documents/Bootcamp_Home folder/homework/Module 3/python_challenge/PyBank/Resources/budget_data.csv")

print(f'                   ')
print(f'Financial Analysis')
print(f'---------------------------')

sum_1 = 0
total_months = 0
changeList = []
dictionary= {}

start_val_set = False
last_val = 0

#open and read csv
with open(budget_data_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    csv_header = next(csv_reader)


    for row in csv_reader:
        
        date_id = row[0]
        value_id = int(row[1]) #Iterated values in profit/losses
        
        
        
        if start_val_set == False:
            last_val = value_id
            start_val_set = True
              
           
         
        total_months += 1 #Iterated total months
        value_id = int(row[1]) #Iterated values in profit/losses
        sum_1 = sum_1 + int(value_id) #Formula for Total Amount
        change = value_id - last_val #Formula to calculate change in values and have it iterated
        last_val = value_id #Restart iterating values in profit/losses to populate into list
        dictionary[date_id] = change

minval = min(dictionary.values())
date_of_min = [k for k, v in dictionary.items() if v==minval]
maxval = max(dictionary.values())
date_of_max = [k for k, v in dictionary.items() if v==maxval]

date_of_min[0]
date_of_max[0]

total_months = len(dictionary.keys())

s = 0
for i in dictionary.values():
    s = s + i
    
s

print("Total Months: " + str(total_months))
print("Total: $" + str(sum_1))
print("Average Change: $" + str(s/(total_months-1)))
print("Greatest Increase in Profits: ", date_of_max[0], (maxval))
print("Greatest Decrease in Profits: ", date_of_min[0], (minval))




import os
import csv

def min_():
    return min(zip(dictionary.keys(), dictionary.values()))

def max_():
    return max(zip(dictionary.keys(), dictionary.values()))
   
#Path to collect data from the resources folder
budget_data_csv = os.path.join("/Users/Justin/Documents/Bootcamp_Home folder/homework/Module 3/python_challenge/PyBank/Resources/budget_data.csv")

print(f'                   ')
print(f'Financial Analysis')
print(f'---------------------------')



sum_1 = 1
total_months = 1
list_1 = []
dictionary= {}

#open and read csv
with open(budget_data_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    csv_header = next(csv_reader)
    
    #Work around to reset reader to restart iteration at line after header
    csv_reader_row1 = next(csv_reader)
    csv_first_row = int(csv_reader_row1[1])
    sum_1 += csv_first_row

    for row in csv_reader:
        
        total_months += 1 #Iterated total months
        value_id = int(row[1]) #Iterated values in profit/losses
        sum_1 = sum_1 + int(value_id) #Formula for Total Amount
        change = value_id - csv_first_row #Formula to calculate change in values and have it iterated
        csv_first_row = value_id #Restart iterating values in profit/losses to populate into list
        list_1.append(change) #Create list to determine total number of months as variable to find the average
        dictionary[row[0]] = row[1]
        
print("Total Months: " + str(total_months))
print("Total: $" + str(sum_1))
print("Average Change: $" + str(sum(list_1)/len(list_1)))
print("Greatest Increase in Profits: ", min_())
print("Greatest Decrease in Profits: ", max_())



   
       


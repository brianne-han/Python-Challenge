# import modules and csv file
import os
import csv
# set file path
csvpath = os.path.join('Resources', 'budget_data.csv')
# open csv reader
with open(csvpath) as budgetfile:
    csvreader = csv.reader(budgetfile,delimiter = ',')
    #print(csvreader)

    # read header row
    csv_header = next(csvreader)
    #print(f"Header: {csv_header}")

    # assign values to variables
    total_months = 0
    total_profit = 0
    changed_value = 0
    last_value = 0
    prof_changed = []
    first_row = True
    date = []
    
    
    # loop through each row after the header
    for row in csvreader:
        date.append(row[0])
        #print(row)
       
       # count the total number of months
        total_months+=1
       # calculate total profit/loss amount
        total_profit+= int(row[1])
        # calculate changes in profits & losses
        if first_row:
            changed_value = 0
            first_row = False
        else:
            changed_value = int(row[1]) - last_value
        prof_changed.append(changed_value)
        last_value = int(row[1])
    total_change = sum(prof_changed)

    # average the changes
    avg_change = round(total_change/total_months, 2)

    # calculate greatest increase in prof over the entire period
    greatest_prof_inc = max(prof_changed)
    # calculate greatest decrease in prof
    greatest_prof_dec = min(prof_changed)
    # date for greatest increase
    greatest_inc_prof_change_date = str(date[prof_changed.index(max(prof_changed))])
    # date for greatest decrease
    greatest_dec_prof_change_date = str(date[prof_changed.index(min(prof_changed))])

# specify the file to write to
output_file = os.path.join("Analysis", "results")
# open the file using write mode
with open(output_file, 'w') as file:
    file.write("Financial Analysis")
    file.write("\n")
    file.write("----------------------")
    file.write("\n")
    file.write(f"Total Months: {total_months}")
    file.write("\n")
    file.write(f"Total: ${total_profit}")
    file.write("\n")
    file.write(f"Average Change: ${avg_change}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {greatest_inc_prof_change_date} (${greatest_prof_inc})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {greatest_dec_prof_change_date} (${greatest_prof_dec})")
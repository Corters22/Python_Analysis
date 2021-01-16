import csv
import os

#joining csv file with code
csvpath = os.path.join("Resources", 'budget_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    
    #calculations and making new lists
    period_change_list = []
    date = []
    prof_loss = []
    row_count = 0
    total =  0
    profit_losses = 0
    for row in csvreader:
        #calculating count of rows
        row_count = row_count + 1
        #calculation total profits/losses
        total = total + int(row[1])
        #calculating changes between two date periods
        profit_losses_2 = int(row[1])
        period_change = profit_losses_2 - profit_losses
        period_change_list.append(period_change)
        #making new lists
        date.append(row[0])
        prof_loss.append(row[1]) 
        #resetting profit loss value
        profit_losses = int(row[1])  

#zipping lists to get max/min and coordinating dates
zippy = zip(date, prof_loss, period_change_list) 
for row in zippy:
    if row[2] == max(period_change_list):
        great_inc_per = row[0]
    elif row[2] == min(period_change_list):
        great_dec_per = row[0]
            
#calculating the total of the profit/loss changes    
total_change = 0
del period_change_list[0]
for value in period_change_list:
    total_change = total_change + value
#calculating avg of profit/loss changes    
avg_change = total_change/ (len(period_change_list))

            
#print to terminal
print("Financial Analysis")
print("--------------------------")
print("Total Months: " + str(row_count))
print("Total: $" + str(total))
print("Average Change: $" + f'{avg_change:.2f}')
print("Greatest Increase in Profits: " + great_inc_per + ' ($' + str(max(period_change_list)) + ')')
print("Greatest Decrease in Profits: " + great_dec_per + ' ($' + str(min(period_change_list)) + ')')

#open new text file
output_path = os.path.join("Analysis", "results.txt")
with open(output_path, 'w', newline='') as textfile:
    #print to text file
    print("Financial Analysis", file=textfile)
    print("--------------------------", file=textfile)
    print("Total Months: " + str(row_count), file=textfile)
    print("Total: $" + str(total), file=textfile)
    print("Average Change: $" + f'{avg_change:.2f}', file=textfile)
    print("Greatest Increase in Profits: " + great_inc_per + ' ($' + str(max(period_change_list)) + ')', file=textfile)
    print("Greatest Decrease in Profits: " + great_dec_per + ' ($' + str(min(period_change_list)) + ')', file=textfile)

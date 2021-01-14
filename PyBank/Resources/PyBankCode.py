import csv
import os

csvpath = os.path.join('budget_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    
    period_change_list = []
    date = []
    prof_loss = []
    row_count = 0
    total =  0
    profit_losses = 0
    for row in csvreader:
        row_count = row_count + 1
        total = total + int(row[1])
        profit_losses_2 = int(row[1])
        period_change = profit_losses_2 - profit_losses
        period_change_list.append(period_change)
        date.append(row[0])
        prof_loss.append(row[1]) 
        profit_losses = int(row[1])  

zippy = zip(date, prof_loss, period_change_list) 
for row in zippy:
    if row[2] == max(period_change_list):
        great_inc_per = row[0]
    elif row[2] == min(period_change_list):
        great_dec_per = row[0]
            
    
total_change = 0
del period_change_list[0]
for value in period_change_list:
    total_change = total_change + value
    
avg_change = total_change/ (len(period_change_list))

            

print("Financial Analysis")
print("--------------------------")
print("Total Months: " + str(row_count))
print("Total: $" + str(total))
print("Average Change: $" + f'{avg_change:.2f}')
print("Greatest Increase in Profits: " + great_inc_per + ' ($' + str(max(period_change_list)) + ')')
print("Greatest Decrease in Profits: " + great_dec_per + ' ($' + str(min(period_change_list)) + ')')



   

    
   


    
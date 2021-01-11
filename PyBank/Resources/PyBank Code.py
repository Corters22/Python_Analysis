import csv
import os
os.path.join("Resources", "budget_data.csv")
#csv_gen = csv.reader("budget_data.csv")
#row_count = 0
#for row in csv_gen:
 #   row_count += 1
#print (f"row count is {row_count}")        
def csv.reader("budget_data.csv"):
    for row in open("budget_data.csv", "r"):
        yield row

   


    
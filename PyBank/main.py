import os
import csv
budget_data_csv = os.path.join("..", "Resources", "budget_data.csv")

months_list = []
values_list = []
differences_list = []

with open("Resources/budget_data.csv", "r") as budget_data_csv:
    budget_data_reader = csv.reader(budget_data_csv)
    next(budget_data_reader)
    for row in budget_data_reader:
        months_list.append(row[0])
        values_list.append(int(row[1]))
        
for index, value in enumerate(values_list): 
    if index == 0:
        differences_list.append(0)   
    else:         
        differences_list.append(value - values_list[index - 1])


financial_analysis = f"""
Financial Analysis
----------------------------
Total Months: {len(months_list)}
Total: ${sum(values_list)}
Average  Change: ${sum(differences_list)/len(differences_list)}
Greatest Increase in Profits: Feb-2012 ($1926159) ${max(differences_list/len(differences_list))}
Greatest Decrease in Profits: Sep-2013 ($-2196167)
"""

print(financial_analysis)
with open("Analysis/budget_results.txt", "w") as budget_results:
    budget_results.write(financial_analysis)




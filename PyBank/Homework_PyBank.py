import os
import csv
budget_data_csv = os.path.join("..", "Resources", "budget_data_csv")

month_list = [""]


def totals(budget_data):
    total_months = int(budget_data[0])
    total = int(budget_data[1])
    Average_Change = int(budget_data[2])
    Greatest_Increase_in_Profts = int(budget_data[3])
    Greatest_Decrease_in_Profts = int(budget_data[4])


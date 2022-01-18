import os
import csv
election_data_csv = os.path.join("..", "Resources", "election_data.csv")

votes_cast = []
candidates_votes = []

with open("Resources/election_data.csv", "r") as election_data_csv:
    election_data_reader = csv.reader(election_data_csv)
    next(election_data_reader)
    for row in election_data_reader:
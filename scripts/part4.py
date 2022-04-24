import time
from datetime import datetime
import re
from pydriller import Repository
import csv

d1 = datetime(2016, 3, 19)
d2 = datetime(2022, 4, 21)
modification_count = {}

for commit in Repository('https://github.com/scipy/scipy.git').traverse_commits():
    for modif in commit.modified_files:
        if re.search('^test_.*\.py$', modif.filename):
            if modif.filename not in modification_count:
                modification_count[modif.filename] = []
                modification_count[modif.filename].append(1)
                modification_count[modif.filename].append(set())
                modification_count[modif.filename][1].add(commit.hash)
                modification_count[modif.filename].append([])
                modification_count[modif.filename][2].append(commit.author_date)
                modification_count[modif.filename][2].append(commit.committer_date)
            else:
                modification_count[modif.filename][0] = modification_count[modif.filename][0] + 1
                modification_count[modif.filename][1].add(commit.hash)
                modification_count[modif.filename][2].append(commit.author_date)
                modification_count[modif.filename][2].append(commit.committer_date)



header = ['Test File', 'Date Added', 'Modification Count', 'Number of People Involved']
with open('E:\PATproject\Part4_output.csv','w',newline='') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    for key in modification_count:
        line = [key, min(modification_count[key][2]), modification_count[key][0], len(modification_count[key][1])]
        writer.writerow(line)
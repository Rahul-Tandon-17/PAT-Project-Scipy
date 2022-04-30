import matplotlib.pyplot as plt
import numpy as np
import csv
import random

## Years Vs Test Files added

data_modification = {}

with open('E:\PATproject\part4_full_file_path.csv','r') as file:
    reader = csv.reader(file)
    for row in reader:
        if row[0] == 'Test File Path':
            continue
        data_modification[row[2][0:4]] = data_modification.get(row[2][0:4], 0) + 1
file.close()

y1 = np.array(list(data_modification.values()))
years_label = list(data_modification.keys())

plt.barh(years_label, y1)
plt.title('Years vs Test Files Added')
plt.xlabel('Number of Test Files Added')
plt.ylabel('Years')
plt.show()

## Most and Least Modified Test Files

file_modification = {}

with open('E:\PATproject\part4_full_file_path.csv','r') as file:
    reader = csv.reader(file)
    for row in reader:
        if row[0] == 'Test File Path':
            continue
        file_modification[row[0]] = file_modification.get(row[0], 0) + int(row[3])
file.close()

top_five = sorted(file_modification.items(), key=lambda x:x[1], reverse=True)
top_test_file = [i[0][i[0].rindex('\\')+1:] for i in top_five[0:5]]
top_test_file_modif_count = [i[1] for i in top_five[0:5]]


low_five = sorted(file_modification.items(), key=lambda x:x[1])
low_test_file = [i[0][i[0].rindex('\\')+1:] for i in low_five[0:5]]
low_test_file_modif_count = [i[1] for i in low_five[0:5]]


plt.barh(top_test_file, top_test_file_modif_count)
plt.title('Top 5 Most Modified Files')
plt.xlabel('Modification Count')
plt.ylabel('Test Files')
plt.show()

plt.barh(low_test_file, low_test_file_modif_count)
plt.xticks([0,1])
plt.title('Top 5 Least Modified Files')
plt.xlabel('Modification Count')
plt.ylabel('Test Files')
plt.show()


###############################################################
#Files with most branches

branch_count = {}

plt.close()

with open(new_path, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        if row[0] == 'Module' or row[0].__contains__('Total')\
                or row[6] in branch_count.values():
            continue
        branch_count[row[0]] = int(row[4])

file.close()

top_5 = sorted(branch_count.items(), key=lambda x:x[1], reverse=True)
top_file = [i[0] for i in top_5[0:5]]
top_branch = [i[1] for i in top_5[0:5]]

plt.barh(top_file, top_branch)
plt.title('Top 5 Files with highest branches')
plt.xlabel('Branch count')
plt.ylabel('Test File')
plt.show()

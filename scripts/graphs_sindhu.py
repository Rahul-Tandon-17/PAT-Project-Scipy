import matplotlib.pyplot as plt
import csv


assertions_count = {}
with open('C:/Users/sindh/College/PAT/PAT-Project-Scipy/output/part2_output.csv','r') as file:
    reader = csv.reader(file)
    for row in reader:
        if row[0] == 'File' or row[0].__contains__('Total'):
            continue
        assertions_count[row[0]] = int(row[1])
file.close()

top_five = sorted(assertions_count.items(), key=lambda x:x[1], reverse=True)
top_files = [i[0] for i in top_five[0:5]]
top_assertions = [i[1] for i in top_five[0:5]]


plt.barh(top_files, top_assertions)
plt.title('Top 5 Files with most Assertions')
plt.xlabel('No of Assertions')
plt.ylabel('Test File')
plt.show()

#############################################################

coverage_count = {}

plt.close()

with open('C:/Users/sindh/College/PAT/PAT-Project-Scipy/output/coverage.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        if row[0] == 'Module' or row[0].__contains__('Total')\
                or row[6] in coverage_count.values():
            continue
        coverage_count[row[0]] = row[6]

file.close()

top_5 = sorted(coverage_count.items(), key=lambda x:x[1], reverse=True)
top_file = [i[0] for i in top_5[0:5]]
top_cov = [i[1] for i in top_5[0:5]]

plt.barh(top_file, top_cov)
plt.title('Top 5 Files with highest coverage')
plt.xlabel('Coverage %')
plt.ylabel('Test File')
plt.show()


###############################################################
#Files with most branches

branch_count = {}

plt.close()

with open('C:/Users/sindh/College/PAT/PAT-Project-Scipy/output/coverage.csv', 'r') as file:
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
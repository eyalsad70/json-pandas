'''
Solve the exact same exercise, but for CSV:
“name” is the first column, “size” is the second column
“max” is the first column, “summary” is the second column
Use “bars.csv” and “summary.csv” respectively
'''
import csv

with open("bars.csv") as f:
    max_bar = None
    summary = 0
    bars = csv.reader(f)
    for bar in bars:
        name = bar[0]
        size = int(bar[1])
        if max_bar is None or size > max_bar[1]:
            max_bar = [name, size]
        summary += size

result = [max_bar[0], summary]

with open("summary.csv", "w") as f:
    csv.writer(f).writerow(result)

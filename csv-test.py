import csv

with open("bars.csv") as f:
    names_lst = []
    for row in csv.reader(f):
        # print(row)
        names_lst.append(row[0])
    maxx = max(names_lst)
    size = len(names_lst)
    result = [maxx, size]
    print(result)
    
with open("summary.csv","w") as fw:
    writer = csv.writer(fw)
    writer.writerow(result)
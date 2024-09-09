import csv

first_label = "Four"
second_label = "Eight"
index_label = ""

def col_to_count(row):
    if row == first_label:
        return 4
    elif row == second_label:
        return 8
    else:
        raise RuntimeError("unexpected row")

col_labels = [first_label, second_label]
row_labels = ["a", "b", "c", "d", "e", "f", "g", "h"]

data = []
for row_label in row_labels:
    row = {}
    row[index_label] = row_label
    for col_label in col_labels:
        row[col_label] = row_label * col_to_count(col_label)
    data.append(row)

with open("data.csv", "w") as f:
    names = [index_label] + col_labels # add empty for index
    writer = csv.DictWriter(f, fieldnames=names)
    writer.writeheader()
    for row in data:
        writer.writerow(row) 
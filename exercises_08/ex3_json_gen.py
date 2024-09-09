import json

first_label = "Three"
second_label = "Five"

def col_to_count(row):
    if row == first_label:
        return 3
    elif row == second_label:
        return 5
    else:
        raise RuntimeError("unexpected row")

col_labels = [first_label, second_label]
row_labels = ["A", "B", "C", "D", "E", "F", "G", "H"]

data = {}
for col_label in col_labels:
    data[col_label] = {}
    for row_label in row_labels:
        data[col_label][row_label] = row_label * col_to_count(col_label)

with open("data.json", "w") as f:
    json.dump(data, f, indent=2)
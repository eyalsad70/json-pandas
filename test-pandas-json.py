import pandas as pd
import json as j

columns = ["three", "five"]
rows = ["A","B", "C", "D", "E", "F"]

def column_value(str):
    if str == "three":
        return 3
    elif str == "five":
        return 5
    else:
        return 0

def create_json_data_file():
    my_data = {}
    for column in columns:
        value = column_value(column)
        my_data[column] = {}
        for row in rows:
            value_str = row * value
            my_data[column][row] = value_str
    print(my_data)

    with open("data.json","w") as fd:
        j.dump(my_data, fd, indent=2)

# create_json_data_file()
df = pd.read_json("data.json")
print(df)

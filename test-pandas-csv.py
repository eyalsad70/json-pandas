import pandas as pd
import csv 

columns = ["Four", "Eight"]
rows = ["A","B", "C", "D", "E", "F"]

def column_value(str):
    if str == "Four":
        return 4
    elif str == "Eight":
        return 8
    else:
        return 0

def create_csv_data_file():
    my_data = []
   
    with open("data.csv","w") as fd:
        writer = csv.writer(fd, lineterminator="\r")
        
        # add 1st line
        first_line = [""]
        for column in columns:
            first_line.append(column)
        writer.writerow(first_line)
        
        for row in rows:
            line = [row.lower()]
            for column in columns:
                value = column_value(column)
                line.append(row.lower() * value)
            my_data.append(line)     
            writer.writerow(line)
        #writer.writerows(my_data)
   
    print(my_data)

    

# create_json_data_file()
create_csv_data_file()

# df = pd.read_json("data.json")
# print(df)

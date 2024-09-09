
import json

with open("bars.json") as f:
    data = json.load(f)
    # print(data)
    names = []
    for item in data:
        names.append(item["name"])
    maxx = max(names)
    size = len(names)
    my_dict = dict()
    my_dict["max"] = maxx
    my_dict["size"] = size
    print(my_dict)

with open("summary.json",'w') as fs:
    json.dump(my_dict, fs)


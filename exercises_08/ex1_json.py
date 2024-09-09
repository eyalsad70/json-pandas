'''
Read a json document from a file called “bars.json”
The document contains a list of bars (dicts)
Each bar is of the form: {“name”: string, “size”: int}
Dump a new document into “summary.json” with indent=2 of the form:
{”max”: “<name of the max>”, “sum”: <the bars size summary>}
Note: you should create the bars.json document manually
'''
import json

with open("bars.json") as f:
    bars = json.load(f)

max_bar = bars[0]
summary = 0
for bar in bars:
    if bar["size"] > max_bar["size"]:
        max_bar = bar
    summary += bar["size"]

result = {
        "max": max_bar["name"],
        "summary": summary,
}

with open("summary.json", "w") as f:
    json.dump(result, f, indent=2)

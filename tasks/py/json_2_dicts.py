#!/usr/bin/env python3
import json
import sys

# Usgae python3 scriptname.py pathtodict
if len(sys.argv) >= 2:
    file = sys.argv[1]
else:
    file = sys.stdin
with open(sys.argv[1], "r") as input:
    str = input.read()
    dict = json.loads(str)
    print(dict)

print(dict['city']) 

inp = {'name': 'Peter', 'surname': 'Muster', 'age': 53, 'hobbies': ['Skifahren', 'Segeln', 'Klettern']}

jsondict = json.dumps(inp)
print(jsondict)

jsonlist = json.dumps(inp["hobbies"])
print(jsonlist)

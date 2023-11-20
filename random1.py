import json

dic = {"name": "Agrima", "age": 21}

with open("file_json.txt", "r") as file:
    y = json.load(file)
    y["friends"].append(dic)
    # x.append(dic)

with open("file_json.txt", "w") as file:
    json.dump(y, file, indent=4)

# a = json.loads(dic)

import json

json_data = '{"name": "Ivan", "age": 25}'

data = json.loads(json_data)

print("Name:", data["name"])
print("Age:", data["age"])

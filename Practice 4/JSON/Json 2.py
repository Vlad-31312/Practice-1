import json

json_data = '''
{
    "fruits": ["apple", "banana", "cherry"],
    "count": 3
}
'''

data = json.loads(json_data)

print("Fruits list:", data["fruits"])
print("First fruit:", data["fruits"][0])
print("Count:", data["count"])

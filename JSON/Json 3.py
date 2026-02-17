import json

json_data = '''
{
  "imdata": [
    {"dn": "eth1/1", "speed": "1000", "mtu": 1500},
    {"dn": "eth1/2", "speed": "inherit", "mtu": 9150}
  ]
}
'''

data = json.loads(json_data)

print("Interface Status")
print("="*40)
print(f"{'DN':10} {'Speed':10} {'MTU':6}")

for item in data["imdata"]:
    print(f"{item['dn']:10} {item['speed']:10} {item['mtu']:6}")

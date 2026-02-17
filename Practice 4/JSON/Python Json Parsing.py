import json

with open("sample-data.json") as f:
    data = json.load(f)

print("Interface Status")
print("=" * 80)
print(f"{'DN':50} {'Description':20} {'Speed':8} {'MTU':6}")
print("-" * 50 + " " + "-" * 20 + "  " + "-" * 6 + "  " + "-" * 6)

for item in data["imdata"]:
    phys = item.get("l1PhysIf")
    if not phys:
        continue

    attrs = phys.get("attributes", {})

    dn = attrs.get("dn", "")
    descr = attrs.get("descr", "")
    speed = attrs.get("speed", "")
    mtu = attrs.get("mtu", "")

    print(f"{dn:50} {descr:20} {speed:8} {mtu:6}")

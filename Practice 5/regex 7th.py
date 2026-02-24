import re
txt=input()
a=re.sub(r"_(.)",lambda m: m.group(1).upper(),txt)
print(a)
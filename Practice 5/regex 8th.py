import re
txt=input()
a=re.findall(r"[A-Z][a-z]*",txt)
result=" ".join(a)
print(result)
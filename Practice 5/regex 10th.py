import re
txt=input()
a=re.sub("([A-Z])",r'_\1',txt).lower()
print(a)
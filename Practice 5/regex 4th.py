import re
txt=input()
a=re.findall("[A-Z][a-z]+",txt)
if a:
    print("Match",a)
else:
    print("No match")
import re
txt=input()
a=re.match("^a.*b$",txt)
if a:
    print("Match",a.group())
else:
    print("No match")
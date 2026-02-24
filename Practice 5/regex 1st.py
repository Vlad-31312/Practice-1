import re
txt=input()
a=re.match("ab*",txt)
if a:
    print("Match",a.group())
else:
    print("No match")
print(a)
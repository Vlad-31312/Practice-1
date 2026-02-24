import re
txt=input()
a=re.match("ab{2,3}",txt)
if a:
    print("Match",a.group())
else:
    print("No match")
print(a)
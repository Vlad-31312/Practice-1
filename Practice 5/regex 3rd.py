import re
txt=input()
a=re.findall("[a-z]+_[a-z]+",txt)
if a:
    print("Match", a)
else:
    print("No match")
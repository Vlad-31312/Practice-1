import re
txt=input()
a=re.sub(r"[ ,\.]",":",txt)
if a:
    print("Match",a)
else:
    print("No match")
import re
txt=input()
result = re.sub(r"(?<!^)([A-Z])", r" \1", txt)
print(result)
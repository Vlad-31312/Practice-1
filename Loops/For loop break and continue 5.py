words = ["привет", "", "как дела", "стоп", "ещё слово"]

for word in words:
    if word == "":
        continue
    if word == "стоп":
        break
    print(word)

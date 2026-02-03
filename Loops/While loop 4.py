while True:
    text = input("Введите текст (exit для выхода): ")
    if text.lower() == "exit":
        break
    if text.strip() == "":
        continue  
    print("Вы ввели:", text)

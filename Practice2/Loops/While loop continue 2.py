while True:
    num = int(input("Введите число (0 для выхода): "))
    if num == 0:
        break
    if num < 0:
        continue 
    print("Вы ввели положительное число:", num)

secret = 5
while True:
    guess = int(input("Угадайте число от 1 до 10: "))
    if guess == secret:
        print("Вы угадали!")
        break
    print("Попробуйте ещё раз")

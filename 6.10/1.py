from random import randint

random_num = randint(1, 100)
cnt = 0
while (True):
    if cnt == 3:
        print("Чисто четное" if random_num % 2 == 0 else print("Число нечетное"))
    guess = -1
    try:
        guess = int(input("Введите число: "))
    except:
        print("Вы ввели не число")
        continue
    if guess == random_num:
        print("Правильно")
        break
    else:
        if guess > random_num:
            print("Загаданное число меньше")
        else:
            print("Загаданное число больше")
        cnt += 1
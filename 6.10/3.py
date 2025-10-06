from random import randint

user_points = 0
bot_points = 0

turns = ["ножницы","камень","бумага"]

while user_points != 3 and bot_points != 3:
    user_turn = input("Введите ход (камень, ножницы, бумага): ")
    if user_turn not in turns:
        print("Ход неверный!")
        user_turn = input("Введите ход (камень, ножницы, бумага): ")
    user_turn = turns.index(user_turn)

    print("---")

    bot_turn = randint(0,2)
    print(f"Ход бота: {turns[bot_turn]}")

    if bot_turn > user_turn or (bot_turn == 0 and user_turn == 2):
        bot_points += 1
    elif bot_turn == user_turn:
        continue
    else:
        user_points += 1

print("вы выиграли" if user_points == 3 else "вы проиграли")



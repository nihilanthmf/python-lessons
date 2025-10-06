def print_pack_report(max_cake_cnt):
    for cake_cnt in range(max_cake_cnt, 0, -1):
        if cake_cnt % 3 == 0 and cake_cnt % 5 == 0:
            print(f"{cake_cnt} - расфасуем по 3 или по 5")
        elif cake_cnt % 5 == 0:
            print(f"{cake_cnt} - расфасуем по 5")
        elif cake_cnt % 3 == 0:
            print(f"{cake_cnt} - расфасуем по 3")
        else:
            print(f"{cake_cnt} - не заказываем!")

print_pack_report(30)
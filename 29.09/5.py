def to_roman(arabic_num):
    # IX = 9
    # VIX = 50 + 9 = 59
    # The symbols are I, V, X, L, C, D, and M, standing respectively for 1, 5, 10, 50, 100, 500, and 1,000

    count_M = arabic_num // 1000
    arabic_num //= 1000 if arabic_num > 1000 else 1
    count_D = arabic_num // 500
    arabic_num //= 500 if arabic_num > 500 else 1
    count_C = arabic_num // 100
    arabic_num //= 100 if arabic_num > 100 else 1
    count_L = arabic_num // 50
    arabic_num //= 50 if arabic_num > 50 else 1
    count_X = arabic_num // 10
    arabic_num //= 10 if arabic_num > 10 else 1
    count_V = arabic_num // 5
    arabic_num //= 5 if arabic_num > 5 else 1
    count_I = arabic_num // 1
    

    return "M" * count_M + "D" * count_D + "C" * count_C + "L" * count_L + "X" * count_X + "V" * count_V + "I" * count_I 

print(to_roman(160))
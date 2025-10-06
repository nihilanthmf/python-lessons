from random import randint

def password_gen(lowercase, uppercase, special_symbols, numbers, length):
    password = []
    symbols = []
    if lowercase == 1:
        symbols.extend(range(ord("a"), ord("z")))
    if uppercase == 1:
        symbols.extend(range(ord("A"), ord("Z")))
    if special_symbols == 1:
        symbols.extend(range(33, 42))
    if numbers == 1:
        symbols.extend(range(48, 57))

    for _ in range(length):
        password.append(chr(symbols[randint(0, len(symbols) - 1)]))

    return "".join(password)

lowercase = int(input("нижний регистр (0, 1): "))
uppercase = int(input("верхний регистр (0, 1): "))
special_symbols = int(input("спец символы (0, 1): "))
numbers = int(input("цифры (0, 1): "))
length = int(input("длина пароля: "))

print(password_gen(lowercase, uppercase, special_symbols, numbers, length))

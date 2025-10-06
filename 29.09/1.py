def ceasar(text, shift, decrypt):
    shift = -1 * shift if decrypt else shift
    text = text.lower()
    result = []
    for s in text:
        if ord(s) + shift > ord("z"):
            current_char = ord("a") + (ord(s) + shift - ord("z")) - 1
        elif ord(s) + shift < ord("a"):
            current_char = ord("z") - (ord(s) + shift - ord("a")) - 1
        else:
            current_char = ord(s) + shift

        result.append(chr(current_char))
    return "".join(result)

inpt = input("строка: ")
shift = int(input("шифт: "))
decrypt = int(input("Дешифровать (0, 1): "))

print(ceasar(inpt, shift, True if decrypt == 1 else False))

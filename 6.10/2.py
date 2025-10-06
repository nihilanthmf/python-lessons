txt = input("Введите текст: ")
txt = txt.lower()

vowel_cnt = 0
consonant_cnt = 0
spaces_cnt = 0
for c in txt:
    if c in "еыаоэяию":
        vowel_cnt += 1
    else:
        consonant_cnt += 1
    if c == " ":
        spaces_cnt += 1

words = txt.split(" ")

words_dict = {}
for w in words:
    if w in words_dict:
        words_dict[w] = words_dict[w] + 1
    else:
        words_dict[w] = 1

print(f"гласных: {vowel_cnt}")
print(f"согласных: {consonant_cnt}")
print(f"пробелов: {spaces_cnt}")
print(f"слов: {len(words)}")
print(f"популярные слова: {[x[0] for x in sorted(words_dict.items(), 
                                  key=lambda word: word[1], reverse=True)[:3]]}")


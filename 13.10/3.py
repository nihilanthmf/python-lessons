s = input()
x = input()
destination = input()

if len(x) > 1:
    print("Error")
    exit(1)

ans = []
x_cnt = 0
for i in s:
    if i != x:
        ans.append(i)
    else:
        x_cnt += 1

for i in range(x_cnt):
    if destination == "end":
        ans.append(x)
    else:
        ans.insert(0, x)

print("".join(ans))
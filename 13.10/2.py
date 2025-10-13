def check_exp(exp):
    if exp.count("(") != exp.count(")"):
        return False
    open_parenthesis_cnt = 0
    for i in range(len(exp)):
        if open_parenthesis_cnt < 0:
            return False
        
        if exp[i] == "(":
            open_parenthesis_cnt += 1
        if exp[i] == ")":
            if open_parenthesis_cnt == 0:
                return False
            else:
                open_parenthesis_cnt -= 1

    return True

exps = [
    "()",
    "100+(10*3)-(34-0)+1",
    "100+(10*3)-(34-0+1",
    "10 + )10(",
]

for e in exps:
    print(check_exp(e))
        
import sys; sys.stdin = open("9012.txt", "r")

T = int(input())
cases = [list(input()) for _ in range(T)]

for case in cases:
    check = []
    for a in case:
        if a == '(':
            check.append('(')
        elif len(check) > 0 and check[-1] == '(' and a == ')':
            check.pop()
        else:
            check.append(')')
            break
    if len(check) == 0:
        print('YES')
    else:
        print('NO')

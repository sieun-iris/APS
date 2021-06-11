import sys; sys.stdin = open("10798.txt", "r")

case = [input() for _ in range(5)]

for i in range(6):
    for j in range(5):
        if (len(case[j])-1) >= i:
            print(case[j][i], end="")
        else:
            continue


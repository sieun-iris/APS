import sys; sys.stdin = open("10798.txt", "r")

case = [input() for _ in range(5)]
maxNum = 0
for i in range(5):
    if len(case[i]) > maxNum:
        maxNum = len(case[i])

for i in range(maxNum):
    for j in range(5):
        if (len(case[j])-1) >= i:
            print(case[j][i], end="")

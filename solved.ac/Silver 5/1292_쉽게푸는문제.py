import sys; sys.stdin = open("1292.txt", "r")

a, b = map(int, input().split())
numList = []
answer = 0

for i in range(1, b+1):
    num = 0
    while num < i:
        if len(numList) > b:
            break
        numList.append(i)
        num += 1

for i in range(a-1, b):
    answer += numList[i]
print(answer)


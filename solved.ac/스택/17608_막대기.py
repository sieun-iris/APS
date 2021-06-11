import sys; sys.stdin = open("17608.txt", "r")

T = int(input())
case = [int(input()) for _ in range(T)]
count = 1
maxNum = case[-1]

for i in range(T-1, -1, -1):
    if case[i] > maxNum:
        maxNum = case[i]
        count += 1

print(count)



